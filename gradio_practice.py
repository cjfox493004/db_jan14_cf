import gradio as gr

def f(x):
    #return x**2
    return 5

iface = gr.Interface(fn = f, inputs = [], outputs = gr.Number())
iface.launch()

#type ctrl and c to stop the server in the terminal