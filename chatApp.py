import tkinter as tk
import time
from chat_App_win import chat_model


chat = chat_model()
def insert_newlines(text, interval=30):
    return '\n'.join(text[i:i+interval] for i in range(0, len(text), interval))

# 发送按钮事件
def sendmessage():
    # 在聊天内容上方加一行 显示发送人及发送时间
    msgcontent = '我: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
    text_msglist.insert(tk.END, msgcontent, ('green', 'right'))
    user_message = text_msg.get('1.0', tk.END)
    text_msg.delete('1.0', tk.END)

    if user_message.strip() == '':
        return
    else:
        wrapped_user_message = insert_newlines(user_message)
        text_msglist.insert(tk.END, wrapped_user_message, 'right')

        msgcontent2 = '轩轩机器人: ' + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n'
        status_label.config(text='轩轩机器人正在输入...')
        root.update_idletasks()
        root.after(1000)
        chat.chat(user_message)
        status_label.config(text='')
        text_msglist.insert(tk.END, msgcontent2, 'blue')
        text_msglist.insert(tk.END, chat.result + '\n', 'left')

if __name__ == "__main__":


    root = tk.Tk()
    root.title('与轩轩机器人的聊天中')
    root.configure(bg='#F0F0F0')  # 更改整个窗口的背景颜色
    # 创建几个frame作为容器
    frame_left_top = tk.Frame(root, bg='#F0F0F0')  # 更改frame的背景颜色
    frame_left_center = tk.Frame(root, bg='#F0F0F0')  # 更改frame的背景颜色
    frame_left_bottom = tk.Frame(root, bg='#F0F0F0')  # 更改frame的背景颜色
    frame_right = tk.Frame(root, bg='#F0F0F0')  # 更改frame的背景颜色

    # 创建需要的几个元素
    text_msglist = tk.Text(frame_left_top, wrap='word', font=('Helvetica', 12,'bold'), bg='#D3D3D3',width=80,height=30)  # 设置背景颜色为灰色
    text_msg = tk.Text(frame_left_center, wrap='word', font=('Helvetica', 12,'bold'), bg='#D3D3D3',width=40,height=15)  # 设置背景颜色为灰色
    button_sendmsg = tk.Button(frame_left_bottom, text='发送', command=sendmessage, height=2, width=10,
                               bg='#80BDFF', activebackground='#64A0E8')  # 调整按钮大小并设置按钮的颜色
    status_label = tk.Label(frame_right, text='', bg='#F0F0F0', font=('Helvetica', 12))  # 创建“正在输入...”标签并设置字体

    # 创建标签，用于设置不同的文本样式
    text_msglist.tag_config('green', foreground='#008B00')  # 用户输入的文本样式
    text_msglist.tag_config('blue', foreground='#0000FF')  # 系统回复的文本样式
    text_msglist.tag_config('right', justify='right')  # 用户输入的对齐方式（右对齐）
    text_msglist.tag_config('left', justify='left')  # 系统回复的对齐方式（左对齐）

    # 使用grid布局，让控件自适应窗口大小
    frame_left_top.grid(row=0, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    frame_left_center.grid(row=1, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    frame_left_bottom.grid(row=2, column=0, sticky=tk.N+tk.S+tk.E+tk.W)
    frame_right.grid(row=0, column=1, rowspan=3, sticky=tk.N+tk.S+tk.E+tk.W)

    # 把元素填充进frame
    text_msglist.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(frame_left_top, command=text_msglist.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_msglist.config(yscrollcommand=scrollbar.set)
    text_msg.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    button_sendmsg.pack(side=tk.RIGHT, padx=5, pady=5)
    status_label.pack(side=tk.TOP, pady=5)

    # 让frame随窗口大小调整而自适应
    root.grid_rowconfigure(0, weight=1)
    root.grid_columnconfigure(0, weight=1)
    frame_left_top.grid_rowconfigure(0, weight=1)
    frame_left_top.grid_columnconfigure(0, weight=1)

    # 主事件循环
    root.mainloop()

