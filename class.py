emails = ["test@hoe.com","regi@gmail.com","saint@yahoo.com","Tesla@mail.com","8micheal@fmail.com"]
print(emails)
newMembers = ["candy@yahoo.com","precious@protonmail.com"]
for new in newMembers:
    emails.append(new)
print(emails)
emails.sort()
print(emails)
lower = []
for low in emails:
    low = low.lower()
    lower.append(low)
print(lower)
lower.pop()
print(lower)
for mail in lower:
    print(f"Welcome {mail} to my wedding")