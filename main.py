def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = count_words(text)
    num_chars = count_characters(text)
    sorted_list = sortdir_tolist(num_chars)
    print(f"---- Report was generated for : {book_path} ----")
    print(f"Number of words in the book: {num_words}")

    for item in sorted_list:
        print(f"The {item["char"]} character was found {item["num"]} times")
    
    print("---- End Report ----")
    


# funcion para abrir el archivo y regresar el file object con read
def get_book_text(path):
    with open(path) as f:
        return f.read()


# función que separa el texto a una lista con cada palabra y realiza un coteo total con el lentgh de la lista
def count_words(text):
    words = text.split()
    return len(words)


# función que realiza un conteo de cada letra en el texto y lo inserta en un diccionario
def count_characters(text):
    lower_text = text.lower() #convierte todo caracter en el string en minuscula
    char_dictionary = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for char in text:
        if char in char_dictionary:
            char_dictionary[char] += 1
    return char_dictionary
 

# función que crea una lista de diccionarios usando el diccionario de letras y conteo como imput. Enlista las letras de mayor a menor ocurrencia.
def sortdir_tolist(dicto):
    sorted_list = []
    for character in dicto:
        sorted_list.append({"char": character, "num": dicto[character]})
    sorted_list.sort(reverse=True, key=lambda dicto: dicto["num"])
    return sorted_list


main()
