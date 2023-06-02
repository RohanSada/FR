import tensorflow as tf
from tensorflow.python.platform import gfile

pb_file_path = './Models/Yolov4/20180408-102900.pb'
saved_model_dir = './Models/MobileNet-SSD_Saved/'

'''
with tf.compat.v1.Session(graph=tf.Graph()) as sess:
    with gfile.FastGFile(pb_file_path, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name='')

builder = tf.compat.v1.saved_model.Builder(saved_model_dir)

# Assuming you know the names of your input and output nodes
input_node_name = 'input'
output_node_name = 'output_node_name'

# Retrieve the input and output nodes from the loaded model
graph = tf.compat.v1.get_default_graph()
input_node = graph.get_tensor_by_name(f'{input_node_name}:0')
output_node = graph.get_tensor_by_name(f'{output_node_name}:0')

# Create input and output signatures for the SavedModel
inputs = {'input': tf.compat.v1.saved_model.utils.build_tensor_info(input_node)}
outputs = {'output': tf.compat.v1.saved_model.utils.build_tensor_info(output_node)}
signature = tf.compat.v1.saved_model.signature_def_utils.build_signature_def(
    inputs=inputs,
    outputs=outputs,
    method_name=tf.compat.v1.saved_model.signature_constants.PREDICT_METHOD_NAME
)

builder.add_meta_graph_and_variables(
    sess,
    [tf.compat.v1.saved_model.tag_constants.SERVING],
    signature_def_map={
        tf.compat.v1.saved_model.signature_constants.DEFAULT_SERVING_SIGNATURE_DEF_KEY: signature
    }
)
builder.save()
'''
import tensorflow as tf
from tensorflow.python.platform import gfile

with tf.compat.v1.Session(graph=tf.Graph()) as sess:
    with gfile.FastGFile(pb_file_path, 'rb') as f:
        graph_def = tf.compat.v1.GraphDef()
        graph_def.ParseFromString(f.read())
        sess.graph.as_default()
        tf.import_graph_def(graph_def, name='')

    num = 0
    # Print all the operations/nodes in the graph
    for op in sess.graph.get_operations():
        print(op.name)
        num+=1
        
