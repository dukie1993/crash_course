guest_list = ["Denis Kolomiets", "Vlad Oborin", "Eugene Kotul", "Pavlo Polishchuk", "Iryna Ponomarenko"]
print("Отправка приглашений")
print(f'{guest_list[0]} - приходи на обед, буду ждать!')
print(f'{guest_list[1]} - приходи на обед, буду ждать!')
print(f'{guest_list[2]} - приходи на обед, буду ждать!')
print(f'{guest_list[3]} - приходи на обед, буду ждать!')
print(f'{guest_list[4]} - приходи на обед, буду ждать!')
print("Приглашения отправлены")

print(f'{guest_list[2]} сказал, что не сможет прийти.')

guest_list[2] = 'Dima Balakhnin'
print("Повторная отправка приглашений")
print(f'{guest_list[0]} - приходи на обед, буду ждать!')
print(f'{guest_list[1]} - приходи на обед, буду ждать!')
print(f'{guest_list[2]} - приходи на обед, буду ждать!')
print(f'{guest_list[3]} - приходи на обед, буду ждать!')
print(f'{guest_list[4]} - приходи на обед, буду ждать!')
print("Приглашения отправлены")

print("Расширение списка гостей")
guest_list.insert(0, "Sasha Pechenkov")
guest_list.insert((len(guest_list) // 2), "Yaroslav Matushevskiy")
guest_list.append("Artem Bratanov")
# print(guest_list)

print("Повторная отправка приглашений")
print(f'{guest_list[0]} - приходи на обед, буду ждать!')
print(f'{guest_list[1]} - приходи на обед, буду ждать!')
print(f'{guest_list[2]} - приходи на обед, буду ждать!')
print(f'{guest_list[3]} - приходи на обед, буду ждать!')
print(f'{guest_list[4]} - приходи на обед, буду ждать!')
print(f'{guest_list[5]} - приходи на обед, буду ждать!')
print(f'{guest_list[6]} - приходи на обед, буду ждать!')
print(f'{guest_list[8]} - приходи на обед, буду ждать!')
print("Приглашения отправлены.")

print(f"Количество приглашённых людей - {len(guest_list)}")

print("На обед приглашаются всего 2 человека.")
pop7 = guest_list.pop(7)
print(f"{pop7} мне очень жаль, но места нет и ты не приглашён больше")
pop6 = guest_list.pop(6)
print(f"{pop6} мне очень жаль, но места нет и ты не приглашён больше")
pop5 = guest_list.pop(5)
print(f"{pop5} мне очень жаль, но места нет и ты не приглашён больше")
pop4 = guest_list.pop(4)
print(f"{pop4} мне очень жаль, но места нет и ты не приглашён больше")
pop3 = guest_list.pop(3)
print(f"{pop3} мне очень жаль, но места нет и ты не приглашён больше")
pop2 = guest_list.pop(2)
print(f"{pop2} мне очень жаль, но места нет и ты не приглашён больше")

print(f'{guest_list[0]} - приходи на обед, приглашение в силе!')
print(f'{guest_list[1]} - приходи на обед, приглашение в силе!')
del guest_list[1]
del guest_list[0]
print(guest_list)