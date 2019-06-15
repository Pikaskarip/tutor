def list_read():
    f = open("C:/Users/Pikas/Desktop/pikas.txt", "r", encoding="utf-8")
    return f.read().split("\n")


def list_write(anime_name):
    anime_list = list_read()
    anime_list.append(anime_name)
    f = open("C:/Users/Pikas/Desktop/pikas.txt", "w", encoding="utf-8")
    f.write("\n".join(anime_list))


def list_remove(anime_to_rem):
    anime_list = list_read()
    if anime_to_rem in anime_list:
        anime_list.remove(anime_to_rem)
        f = open("C:/Users/Pikas/Desktop/pikas.txt", "w", encoding="utf-8")
        f.write("\n".join(anime_list))
        return True
    return False


def gen_html():
    f_template = open("C:/Users/Pikas/Desktop/pikas_template.html", "r", encoding="utf-8").read()
    anime_html_to_add = ""
    for c in list_read():
        if c:
            anime_html_to_add += "<tr><td>{}</td></tr>".format(c)
    if not anime_html_to_add:
        return False
    f_template = f_template.replace("<!-- место для списка онимэ -->", anime_html_to_add)
    f = open("C:/Users/Pikas/Desktop/pikas.html", "w", encoding="utf-8")
    f.write(f_template)
    return True
