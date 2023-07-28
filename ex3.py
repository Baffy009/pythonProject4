# Возьмите задачу о банкомате из семинара. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.


def put_money(cash_1_op, count_1_op):
    """Функция для внесения денег"""
    add = float(input("внесите сумму кратную 50: "))
    if add % 50 == 0:
        cash_1_op += add
        count_1_op += 1
        op_history.append(f"пополнение счета на {str(add)} у.е, баланс: {round(cash_1_op, 2)} у.е")
        return cash_1_op, count_1_op
    else:
        print("! ошибка внесения денег: неверная сумма")
        op_history.append("ошибка внесения денег: неверная сумма")
        count_1_op += 1
        return cash_1_op, count_1_op


def give_money(cash_2_op, count_2_op):
    """Функция для снятия денег"""
    take = float(input("введите сумму снятия кратную 50: "))
    if take % 50 == 0:
        percent = take * 1.5 * 0.01
        if percent < 30:
            percent = 30
        if percent > 600:
            percent = 600

        if cash_2_op < (take + percent):
            print("! ошибка снятия денег: недостаточно средств")
            op_history.append("ошибка снятия денег: недостаточно средств")
            count_2_op += 1
            return cash_2_op, count_2_op
        else:
            cash_2_op -= (take + percent)
            count_2_op += 1
            op_history.append(f"снятие {str(take)} у.е, баланс: {round(cash_2_op, 2)} у.е")
            return cash_2_op, count_2_op
    else:
        print("! ошибка снятия денег: неверная сумма")
        op_history.append("ошибка снятия денег: неверная сумма")
        count_2_op += 1
        return cash_2_op, count_2_op


def print_history(print_op_history):
    """Функция для печати истории операций"""
    print("\nистория операций: ")
    print(" \n".join(print_op_history))
    input("для продолжения нажмите любую клавишу...")




# входные данные и запуск банкомата
cash = 0
operation_counter = 0
op_history = []
