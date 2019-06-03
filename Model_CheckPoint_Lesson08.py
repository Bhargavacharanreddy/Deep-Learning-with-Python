from keras.callbacks import ModelCheckpoint
...
checkpoint = ModelCheckpoint('weights.best.hdf5', monitor='val_acc', save_best_only=True, mode='max')
callbacks_list = [checkpoint]
# Fit the model
model.fit(..., callbacks=callbacks_list)