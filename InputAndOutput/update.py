def replace(input):
        with open(input,"r") as f:
            content=f.read()
        update_content=content.replace("Java","python")

        with open(input,"w") as f:
              content=f.write(update_content)


replace("practice.txt")
