# CommandGen
Speedrun Practice Command Generator for Minecraft 1.13+

<img src="https://user-images.githubusercontent.com/110107468/191931244-cfc5b6d9-a166-4d7d-8cce-b540b522f097.png" width="50%"/>

## How does this work?

- Download the .exe file in the latest release.
- Preset items are shown above.
- Modify items in the inventory and offhand by entering the lowercase name of the item in a new line, followed by a space and the quantity of that item.
  - The first nine lines of the inventory will be your hotbar, in that order.
  - For Potions of Fire Resistance and Splash Potions of Fire Resistance, type "fire_res" and "splash_fire_res" respectively.
- Select "Golden Helmet" and/or "Soul Speed Boots" to be equipped with that item (selecting "Soul Speed Boots" gives you Iron Boots enchanted with Soul Speed II).
- You can choose the dimension the command takes you to with the drop-down menu at the top.
  - "Overworld" results in the command to leaving you where you are.
  - "Nether" results in the command creating a nether portal.
  - "End" results in the commmand creating an end portal.
- Click "Generate", then "Copy". This copies a `/give` command that gives you the command block.
- Since the `/give` command is too long to run in the Minecraft chat, you'll have to paste it in a command block and activate that command block (e.g. placing and clicking a button next to it).

<img src="https://user-images.githubusercontent.com/110107468/182213404-bffb524c-8242-4573-89a2-2b55ea4a532c.png" width="75%"/>

- Activating that command block gives you a separate command block (this is the one you might want to save to your hotbar). Placing this command block gives you all the items and sends you to the nether.

## Credits

woofdoggo - falling block command

Duncan - end fight block generator
