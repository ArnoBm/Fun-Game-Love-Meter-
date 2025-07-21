import random
import time
from datetime import datetime, timedelta

print("💖 Welcome to the Love Meter Game 💖\n")

# Input Section
boy = input("Enter the Boyfriend's name: ")
girl = input("Enter the Girlfriend's name: ")

boy_bday = input(f"🎂 Enter {boy}'s birthday (YYYY-MM-DD): ")
girl_bday = input(f"🎂 Enter {girl}'s birthday (YYYY-MM-DD): ")
anniversary = input("💞 Enter your anniversary date (YYYY-MM-DD): ")

# Convert string dates to datetime objects
try:
    boy_bday = datetime.strptime(boy_bday, "%Y-%m-%d")
    girl_bday = datetime.strptime(girl_bday, "%Y-%m-%d")
    anniversary = datetime.strptime(anniversary, "%Y-%m-%d")
except:
    print("⚠️ Invalid date format! Please use YYYY-MM-DD.")
    exit()

print("\nCalculating Love Percentage...")
time.sleep(1.5)

# Love score logic: more random, but based slightly on shared bday digits
love_score = random.randint(30, 100)
if boy_bday.day == girl_bday.day or boy_bday.month == girl_bday.month:
    love_score += 5  # little boost if birthday same day or month
if anniversary.day == boy_bday.day or anniversary.day == girl_bday.day:
    love_score += 5

love_score = min(love_score, 100)

print(f"\n💘 Love percentage between {boy} and {girl} is: {love_score}%")

# Determine possibility of marriage
if love_score > 85:
    message = "💍 Perfect match! Wedding bells are ringing! 💒"
    days_until_marriage = random.randint(30, 180)
elif love_score > 60:
    message = "❤️ Strong bond! Marriage is very likely!"
    days_until_marriage = random.randint(181, 730)
elif love_score > 40:
    message = "🙂 There's potential, but work is needed."
    days_until_marriage = random.randint(731, 1825)
elif love_score > 25:
    message = "💔 Hmmm, some serious effort required!"
    days_until_marriage = random.randint(1826, 3650)
else:
    message = "😢 Sorry... not much hope. Try again in your next life!"
    days_until_marriage = None

print(f"\n🔮 Prediction: {message}")

# Show marriage prediction date
if days_until_marriage:
    marriage_date = datetime.now() + timedelta(days=days_until_marriage)
    print(f"📅 Probable Marriage Day: {marriage_date.strftime('%A, %d %B %Y')}")

    # Fun twist: check how many days since anniversary
    days_since_anniversary = (datetime.now() - anniversary).days
    print(f"💞 You have been together for {days_since_anniversary} days!")
else:
    print("📅 Marriage Day: Uncertain ❌")

# Birthday compatibility note
if boy_bday.month == girl_bday.month:
    print("🎉 Bonus: You both were born in the same month! Cosmic match!")
if boy_bday.day == girl_bday.day:
    print("🎊 Whoa! You both share the same birthday! Rare connection!")

# Fun feature: Who will cheat (for humor only)
print("\n🤔 Detecting possible cheater...")
time.sleep(1.5)
cheat_possibility = random.choices(
    [boy, girl, "Neither"], weights=[30, 30, 40], k=1
)[0]

if cheat_possibility == "Neither":
    print("😇 Both are loyal! Trust level: 100% ❤️")
else:
    print(f"😱 Uh-oh! There is a chance {cheat_possibility} might cheat! (Just kidding... or not 😏)")
