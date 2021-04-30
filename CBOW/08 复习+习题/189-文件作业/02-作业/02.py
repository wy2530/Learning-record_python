# # 注册
# user_info = {}
# with open('login.txt', mode='r', encoding='utf-8') as f:
#     for line in f:
#         user, pwd = line.strip().split(" ")
#         user_info[user] = pwd
# print("所有用户的数据：", user_info)
#
# while True:
#     new_name = input("请输入你的名字：")
#     if new_name in user_info:
#         print("用户名已存在，请重新输入")
#         continue
#
#     pwd = input("请输入密码：")
#     re_pwd = input("请再次输入密码：")
#     if pwd == re_pwd:
#         # dict.update("{}:{}".format(new_name, pwd))
#         with open('login.txt', mode='a', encoding='utf-8') as f1:
#             f1.write('\n{} {}'.format(new_name, pwd))
#             print("注册成功")
#             break
#     else:
#         print("请重新输入密码")


