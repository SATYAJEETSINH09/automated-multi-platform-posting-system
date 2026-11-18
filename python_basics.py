
# 1. Store message
message = "Check out our latest business platform. https://example.com"

# 2. Store platforms
platforms = ["LinkedIn", "Facebook", "X", "Reddit", "Telegram"]

# 3. Create function
def display_message(message):
    print("Message:", message)


# 4. Create class
class Posting:
    def show_platform(self, platform):
        print("Platform:", platform)


# 5. Create object
posting = Posting()

# 6. Display message
display_message(message)

# 7. Display all platforms
for platform in platforms:
    posting.show_platform(platform)

# 8. Exception handling
try:
    print(10 / 0)
except Exception as error:
    print("Error:", error)

print("Program completed!")
