import tensorflow as tf

try:
    path = '/app/datasets/dataset_1/dataset_1-r07.tfrecords'

    raw_dataset = tf.data.TFRecordDataset(path)

    for raw_record in raw_dataset:
        example = tf.train.Example()
        example.ParseFromString(raw_record.numpy())
        print(example)

except Exception as e:
    print("Exception Caught\n\n{}".format(e))