client.event

async def on_ready():

    x = "global"

    def foo():
        print("x inside :", x)

    foo()
    print("x outside:", x)

global amounts

try:

    with open('main.py', 'w') as f:
        f.write('Hi there!')

with open('amounts.json') as f:

amounts = json.load(f)

except FileNotFoundError:

print("Could not load amounts.json")

amounts = {}


@client.command(pass_context=True)
