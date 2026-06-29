import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV3Small
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model

# -------------------------
# PATHS
# -------------------------
train_path = r"C:\Users\ASUS\Downloads\archive\PlantVillage\train"
val_path   = r"C:\Users\ASUS\Downloads\archive\PlantVillage\val"

# -------------------------
# IMAGE SETTINGS
# -------------------------
img_size = (224, 224)
batch_size = 32

# -------------------------
# DATA AUGMENTATION (IMPORTANT FIX)
# -------------------------
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=25,
    width_shift_range=0.2,
    height_shift_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(rescale=1./255)

train_data = train_datagen.flow_from_directory(
    train_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical'
)

val_data = val_datagen.flow_from_directory(
    val_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical'
)

# -------------------------
# BASE MODEL (PRETRAINED)
# -------------------------
base_model = MobileNetV3Small(
    weights='imagenet',
    include_top=False,
    input_shape=(224, 224, 3)
)

# -------------------------
# STEP 1: TRAIN HEAD ONLY (already partially done)
# -------------------------
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.3)(x)
x = Dense(128, activation='relu')(x)
output = Dense(train_data.num_classes, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=output)

# -------------------------
# COMPILATION (HEAD TRAINING)
# -------------------------
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=0.001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# -------------------------
# TRAIN HEAD (SHORT PHASE)
# -------------------------
print("Training top layers...")
model.fit(
    train_data,
    validation_data=val_data,
    epochs=3
)

# -------------------------
# STEP 2: FINE TUNING (IMPORTANT PART)
# -------------------------

# Unfreeze last layers of MobileNetV3
base_model.trainable = True

# Freeze early layers, train last 30 layers
for layer in base_model.layers[:-30]:
    layer.trainable = False

# IMPORTANT: lower learning rate for fine-tuning
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-5),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# -------------------------
# FINE TUNE TRAINING
# -------------------------
print("Fine-tuning model...")
model.fit(
    train_data,
    validation_data=val_data,
    epochs=5
)

# -------------------------
# SAVE MODEL
# -------------------------
model.save("fasal_sanjeevani_model_finetuned.h5")

print("Training completed and model saved!")