from curses import raw
import tensorflow as tf

@tf.function
def _inspect_tfrecords(path):
    raw_dataset = tf.data.TFRecordDataset(path)

    print(raw_dataset)

    # data_summary = {}

    # for data in raw_dataset:
    #     entry_shape = str(data.shape)

    #     # print(str(data.shape))

    #     if entry_shape not in data_summary.keys():
    #         entry_shape[entry_shape] = 0

    #     entry_shape[entry_shape] = entry_shape[entry_shape] + 1

    # print(data_summary)

@tf.function
def _print_tfrecords_examples(path):
    raw_dataset = tf.data.TFRecordDataset(path)

    print(raw_dataset)

    for raw_record in raw_dataset:
        print(raw_record)

        # example = tf.train.Example()
        # example.ParseFromString(raw_record.numpy())
        # print(example)
        continue

try:
    path = '/app/datasets/dataset_1/dataset_1-r07.tfrecords'

    _inspect_tfrecords(path)

    # _print_tfrecords_examples(path)

except Exception as e:
    print("Exception Caught\n\n{}".format(e))



 # raw_image_dataset = tf.data.TFRecordDataset(path)

    # # Create a dictionary describing the features.
    # image_feature_description = {
    #     'height': tf.io.FixedLenFeature([], tf.int64),
    #     'width': tf.io.FixedLenFeature([], tf.int64),
    #     'depth': tf.io.FixedLenFeature([], tf.int64),
    #     'label': tf.io.FixedLenFeature([], tf.int64),
    #     'image_raw': tf.io.FixedLenFeature([], tf.string),
    # }

    # def _parse_image_function(example_proto):
    #     # Parse the input tf.train.Example proto using the dictionary above.
    #     return tf.io.parse_single_example(example_proto, image_feature_description)

    # parsed_image_dataset = raw_image_dataset.map(_parse_image_function)
    
    # print(parsed_image_dataset)