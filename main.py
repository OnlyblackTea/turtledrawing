from turtle import *
import stack as st

stack = st.stack()

footLength = 200  # 步长
LineSize = 16  # 线宽
Angle = 30  # 角度
colormode(255)  # 设置颜色模式
lt(90)  # 将turtle转为向上

setup(800, 800, 0, 0)   # 初始化
pu()                    #
goto(0, -300)           #
pd()                    #

g = 0
speed("fastest")


def walk(depth):
    if depth == 13:
        return
    else:
        # 预处理
        global g, footLength, LineSize
        g = depth * 20  # 按深度上色
        if g > 255:  # 防止溢出
            g = 255
        pencolor(5, g, 5)  # 设置颜色变绿
        footLength = footLength * 0.77  # 每递归一层步长减少
        LineSize = LineSize * 0.8  # 每递归一层宽度减少
        width(LineSize)

        # 开始画画
        fd(footLength)  # 画出当前线
        stack.insert(pos())  # 记录当前位置
        rt(Angle)
        walk(depth + 1)  # 画右边
        lt(Angle * 2)
        walk(depth + 1)  # 画左边
        rt(Angle)
        stack.pop()  # 弹出当前位置

        pu()
        goto(stack.top())  # 返回上一层位置
        pd()

        # 回溯
        LineSize = LineSize / 0.8
        width(LineSize)
        footLength = footLength / 0.77


if __name__ == '__main__':
    stack.insert(pos())  # 保存初始位置
    walk(0)  # 进入递归
    done()  # 保留结果
