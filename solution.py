import pandas as pd
import numpy as np


chat_id = 854074776 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:
  null_x = x_success * 100/x_cnt
  stat, pval = proportions_ztest(count = y_success, nobs=  x_success, value= null_x)


    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return pval > 0.07 # Ваш ответ, True или False
