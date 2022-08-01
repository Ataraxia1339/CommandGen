from tkinter import *
import re


def parse(line):
    size = ""
    item = line
    try:
        index = re.search(" \d+", line).span()[0]
        size = re.search(r"\d+", line[index:]).group()
        item = line[:index]
    except:
        size = "1"
    item = item.replace(" ", "_")
    if item == "":
        return "iron_axe 0"
    while item[-1] == "_":
        item = item[:-1]
    if item == "fire_res":
        return r"potion{Potion:\"minecraft:fire_resistance\"} " + size
    if item == "splash_fire_res":
        return r"splash_potion{Potion:\"minecraft:fire_resistance\"} " + size
    return item + " " + size


def generate():
    copy["text"] = "Copy"
    res = "give @p command_block{CustomModelData:1,BlockEntityTag:{Command:\"/summon falling_block ~ ~1 ~ {Time:1," \
          "BlockState:{Name:redstone_block},Passengers:[{id:falling_block,Passengers:[{id:falling_block,Time:1," \
          "BlockState:{Name:activator_rail},Passengers:[{id:command_block_minecart,Command:'gamerule" \
          "commandBlockOutput false'}, {id:command_block_minecart,Command:'clear @a'},"

    for line in inventory.get("0.0", "end").split("\n"):
        if line == "":
            pass
        items = parse(line)
        res += "{id:command_block_minecart,Command:'give @a " + items + "'},"

    oh = offhand.get()
    if oh != "":
        oh = parse(oh)
        res += "{id:command_block_minecart,Command:'replaceitem entity @p weapon.offhand " + oh + "'},"

    if ghcheck.get() == 1:
        res += "{id:command_block_minecart,Command:'replaceitem entity @p armor.head golden_helmet'},"

    if ssbcheck.get() == 1:
        res += "{id:command_block_minecart,Command:'replaceitem entity @p armor.feet " \
               "iron_boots{Enchantments:[{id:soul_speed,lvl:2}]}'},"

    res += "{id:command_block_minecart,Command:'execute as @a run setblock ~ ~5 ~ nether_portal'}," \
           "{id:command_block_minecart,Command:'execute as @a run tp @a ~ ~5 ~'},{id:command_block_minecart," \
           "Command:'setblock ~ ~1 ~ command_block{auto:1,Command:\\\"fill ~ ~ ~ ~ ~-3 ~ air\\\"}'}," \
           "{id:command_block_minecart,Command:'kill @e[type=command_block_minecart,distance=..1]'}]}]}]}\", " \
           "auto:1b}, display:{Name:'{\"text\":\"Command Block\",\"italic\":false}'}}"
    result.delete(0, END)
    result.insert(0, res)


def copy():
    root.clipboard_clear()
    root.clipboard_append(result.get())
    root.update()
    copy["text"] = "Copied!"


if __name__ == "__main__":
    root = Tk()
    root.title("Command Generator")
    root.geometry("700x700")
    root.resizable(False, False)
    for i in range(5):
        root.grid_columnconfigure(i, weight=1)

    ghcheck = IntVar()
    ssbcheck = IntVar()
    ghelmet = Checkbutton(root, text="Golden Helmet", font=("Consolas", 16), variable=ghcheck)
    ghelmet.grid(row=0, column=0, columnspan=2, padx=80, pady=10)
    ssboots = Checkbutton(root, text="Soul Speed Boots", font=("Consolas", 16), variable=ssbcheck)
    ssboots.grid(row=0, column=2, columnspan=2, pady=10)
    l1 = Label(root, text="Offhand slot:", font=("Consolas", 16))
    l1.grid(row=1, column=0, sticky="E", pady=10)
    offhand = Entry(root, font=("Consolas", 16), width=40)
    offhand.insert(0, "golden_carrot 64")
    offhand.grid(row=1, column=1, columnspan=4, pady=10)
    l2 = Label(root, text="Inventory:", font=("Consolas", 16))
    l2.grid(row=2, column=0, sticky="E", pady=5)
    inventory = Text(root, width=40, height=18, font=("Consolas", 16))
    inventory.insert("0.0", "iron_axe\niron_pickaxe\niron_shovel\ncrafting_table\nobsidian 64\nflint_and_steel\n"
                            "nether_bricks 32\nender_pearl 16\nlava_bucket\nblaze_rod 7\nstring 96\nacacia_planks 22\n"
                            "glowstone_dust 64\nacacia_boat\ngolden_pickaxe\nender_pearl 16\ncrying_obsidian 64\n"
                            "splash_fire_res\nnetherrack 64\nfire_res\nsoul_sand 64\ngravel 64")
    inventory.grid(row=2, column=1, columnspan=4, pady=5)
    generate = Button(root, text="Generate", font=("Consolas", 16), command=generate, width=46,
                      bg="#008080", fg="White")
    generate.grid(row=3, column=0, columnspan=5, pady=15)
    result = Entry(root, font=("Consolas", 16), width=34)
    result.grid(row=4, column=0, columnspan=4, pady=10, sticky="W", padx=70)
    copy = Button(root, text="Copy", font=("Consolas", 16), command=copy, width=10, bg="#6A5ACD", fg="White")
    copy.grid(row=4, column=3, sticky="E")

    root.mainloop()
