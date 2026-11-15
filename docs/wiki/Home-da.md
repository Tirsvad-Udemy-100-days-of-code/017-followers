[English](Home) · **Dansk** · [Bahasa Melayu](Home-ms)

# Followers

Et lille eksempel på, hvordan man definerer og bruger en Python-klasse.

## Hvad er det?

Dag 17 af Udemy-kurset *100 Days of Code: The Complete Python Pro Bootcamp*. Klassen `User` i `src/main.py` viser, hvordan en klasse defineres og bruges. Det er kun en demonstration: den har ingen tests og ingen afhængigheder.

## Hvad øvelsen lærer dig

- At definere en klasse med en konstruktør (`__init__`), der sætter attributter med standardværdier
- Instansattributter: `id`, `username`, `followers` og `following`
- At skrive en metode (`follow`), der ændrer tilstanden i to objekter på én gang

## Hvad det gør

- Opretter to brugere og lader den første følge den anden
- Når `user_1.follow(user_2)` kører, stiger både `user_1.following` og `user_2.followers` med én
- Udskriver de fire tællere, så det forventede output er 0, 1, 1 og 0

## Videre

- [Kom godt i gang](Getting-Started-da)
- [Projektdokumenter](Project-Documents-da)
