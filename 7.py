import matplotlib.pyplot as plt

kunlar = ["Du", "Se", "Cho", "Pa", "Ju", "Sha", "Ya"]
sarf = [42, 38, 51, 47, 62, 70, 45]
ortacha = sum(sarf) / 7
print("O'rtacha sarf: ", ortacha)
plt.plot(kunlar, sarf, marker='o', label='Sarf')
plt.axhline(y=ortacha, color='r', linestyle='--', label='Ortacha sarf')
for i in range(7):
    if sarf[i] > ortacha:
        plt.scatter(kunlar[i], sarf[i], label='Yuqori yuqori' if i==2 else"")
plt.legend()


plt.title("Kunlik sarf")
plt.xlabel("Kunlar")
plt.ylabel("Sarf")

plt.savefig("Imtihon/kunlik_sarf.png")
