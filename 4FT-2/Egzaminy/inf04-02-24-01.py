'''
************************************************
 klasa:     Znaki
 opis:      klasa implementuje narzędzia do zmiennych typu łańcuchowego (string)
 metody:    licz_samogloski - liczba całkowita oznaczająca ilość samogłosek występujących w tekście
            usun_powtorzenia_obok_siebie - łańcuch wejściowy z usuniętymi znakami występującymi obok siebie
 autor:     12345678910
************************************************
'''
class Znaki:
    @staticmethod
    def licz_samogloski(text:str) -> int:
        samogloski = "aąeęiouóyAĄEĘIOUÓY"
        samogloski_count = 0
        if len(text) == 0:
            return 0
        for letter in text:
            if letter in samogloski:
                samogloski_count += 1
        return samogloski_count
    @staticmethod
    def usun_powtorzenia_obok_siebie(text:str) -> str:
        lancuch = ""
        if len(text) == 0:
            return ""
        last_letter = ""
        for letter in text:
            if last_letter == "":
                last_letter = letter
                lancuch += letter
                continue
            else:
                if letter == last_letter:
                    last_letter = letter
                    continue
                else:
                    last_letter = letter
                    lancuch += letter
        return lancuch
if __name__ == "__main__":
    tekst = input("Podaj tekst: ")
    print(f"Liczba samogłosek: {Znaki.licz_samogloski(tekst)}")
    print(f"Łańcuch po usunięciu duplikatów: {Znaki.usun_powtorzenia_obok_siebie(tekst)}")
