import random

even = 0
odd = 0

my_num = random.randint(1, 20)

if my_num % 2 == 0:
    even = 1
else:
    odd = 1

print(even)
print(odd)

pick = input(f"\n\nHeads or Tails? ").lower()

if pick == 'heads':
    if even == 1:
        print(f"\nYou picked HEADS! Fuck yeah! 🎉 \n")
    else:
        print(f"\nSorry it was tails you lose.\n")
elif pick == 'tails':
    if odd == 1:
        print(f"\nYou picked TAILS!! Noyce! ⛔️ \n")
    else:
        print(f"\nIt was heads and you lose. Fuck you.\n")
else:
    print(f"\nGet the fuck outta here!\n")