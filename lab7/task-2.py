import task1
import wikipedia

wikipedia.set_lang("ru")
stress = wikipedia.page("Стресс")
string = stress.content


f = open('stress.txt')
contents = f.read()

arr = contents.split()

charcnt = len(contents)
plagcharcnt = 0


for i in range(0, len(arr) - 2):
    key = arr[i] + ' ' + arr[i+1] + ' ' + arr[i+2]
    if task1.boyer_moore_horspool(string, key) > 0:
        plagcharcnt += len(key)

print(f'Текст является плагиатом на {plagcharcnt/charcnt * 100} процентов')
