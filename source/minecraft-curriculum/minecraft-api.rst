.. _minecraft-api:

Minecraft API
=============

Minecraft Pi er Python tól sem kemur uppsett á Raspberry Pi (RasPi hér eftir). Við skulum skoða þau Minecraft tólin og aðgerðir þeirra.

.. note::
    Minecraft Pi er ekki full útgáfa af upprunalega leiknum.

Minecraft Pi tólin eru geymd í möppunni *mcpi*. Tólin hafa síðan klasa sem allir hafa nokkrar aðgerðir til að stjórna Minecraft.

Klasarnir sem við getum notað eru *Minecraft*, *Block*, *Event* og *Vec3*.

Hver klasi hefur svo nokkrar aðgerðir.

Til að sækja klasana getum við notað *import* skipunina (sjá :ref:`minecraft-our-tools`). Við þurfum einnig að tilgreina möppuna og skrána sem klasinn er geymdur í.

*Dæmi*

>>> from mcpi.minecraft import Minecraft

Hér erum við að sækja *Minecraft* klasann í möppunni *mcpi* sem er geymdur í skránni *minecraft.py*.

Við getum einnig sótt klasann *Block* sem er geymdur í skránni *block.py*

*Dæmi*

>>> from mcpi.block import Block

Taktu eftir að við sleppum *.py* endingunni þegar við vísum í skrána sem klasinn er geymdur í.

Ef við kíkjum í *minecraft.py* skrána þá sjáum við svolítið athyglisvert. Efst í skránni er verið að sækja alla klasana sem við ætlum að nota. Um leið og við sækjum *minecraft.py* þá fáum við aðgang að öllum aðgerðum í hinum klösunum án þess að þurfa að sækja þá sérstaklega. Það er því óþarfi að sækja þá sérstaklega því *minecraft.py* gerir það fyrir okkur.

.. code-block:: python

    from connection import Connection
    from vec3 import Vec3
    from event import BlockEvent
    from block import Block


.. module:: minecraft

.. class:: Minecraft
    
    Klasi af aðgerðum sem við getum notað til að stýra leiknum.

    .. method:: create(address = "localhost", port = 4711)

        Býr til tengingu við Minecraft leik á þeirri hýsitölvu sem er skilgreind. Localhost er þín eigin tölva. Þú getur einnig skilgreint IP töluna á annari tölvu sem þú ert tengdur til að spila Minecraft í heimi með öðrum spilurum.

        *Dæmi:*

        >>> from mcpi.minecraft import Minecraft
        >>> mc = Minecraft.create("192.168.1.1", 4711)


    .. method:: postToChat(skilaboð)

        Sendir texta á skjáinn í leiknum.

        *Dæmi*

        >>> from mcpi.minecraft import Minecraft
        >>> mc = Minecraft.create()
        >>> mc.postToChat("Veiii.. minecraft er skemmtilegt")

    .. method:: getBlock(x, y, z)

        Sækir tegund blokkarinnar á gefnu hniti og skilar tilbaka auðkenni blokkarinnar.

        *Dæmi*

        >>> from mcpi.minecraft import Minecraft
        >>> mc = Minecraft.create()
        >>> mc.getBlock(3, 7, 9)
        0

        .. todo::

            Vantar result

    
    .. method:: setBlock(x, y, z, block.id)

        Setur nýja blokk af tegundinni *block.id* á hnitið.

        *Dæmi*

        Setur *STONE* á hnitið *3, 7, 9*

        >>> from mcpi.minecraft import Minecraft
        >>> mc = Minecraft.create()
        >>> mc.setBlock(3, 7, 9, 1)

        .. todo::

            Vantar result

    .. attribute:: player

        Tilviksbreyta með upplýsingum um Steve og aðgerðum til að stjórna honum, sjá :class:`~minecraft.CmdPlayer`

        *Dæmi*

        >>> from mcpi.minecraft import Minecraft
        >>> mc = Minecraft.create()
        >>> mc.player.getPos()

    .. attribute:: events

        Tilviksbreyta sem fær tilkynningu um leið og Steve lemur í blokk með sverði, sjá :class:`~minecraft.CmdEvents`.

        *Dæmi*

        .. code-block:: python
            
            from mcpi.minecraft import Minecraft
            mc = Minecraft.create()

            while True:
                print(mc.events.pollBlockHits())


.. class:: CmdPlayer

    Klasi með aðgerðum til að láta Steve gera allskyns kúnstir. Tilvik af þessum klasa koma innifalinn með :class:`~minecraft.Minecraft` svo að það skal ekki nota hann beint.


    .. method:: getPos()

        Sækir staðsetninguna á Steve í leiknum sem Vec3

        *Dæmi*

        >>> from mcpi.minecraft import Minecraft
        >>> mc = Minecraft.create()
        >>> mc.player.getPos()

    .. method:: setPos(x,y,z)

        Færir Steve um stað í Minecraft með því að nota brotatölur sem x, y, z hnit.


        *Dæmi*
        
        >>> from mcpi.minecraft import Minecraft
        >>> mc = Minecraft.create()
        >>> mc.player.setPos(1.9, 5.7, 10.3)


.. class:: CmdEvents
    
    Klasi með aðgerð sem skilar lista með upplýsingum um hvert högg sem var gert með *sverði*. Hægt er að sækja fjölda högga með aðgerðinni :meth:`~minecraft.CmdEvents.pollBlockHits`. Inniheldur einnig aðgerð til að endursetja.

    Í klasanum :class:`~minecraft.Minecraft` er tilviksbreytan :attr:`~minecraft.Minecraft.events` sem býr til eintak af þessum klasa svo það er óþarfi að nota þennan klasa beint.


    .. method:: clearAll(self)

        Hreinsar tilkynningarlistann.


    .. method:: pollBlockHits(self)

        Skilar tilbaka upplýsingum um blokkina sem var lamið í. Athugaðu að það er eingöngu hægt að nota sverð.



.. _block-constants:

Auðkenni allra blokka í Minecraft
---------------------------------

.. code-block:: python

    AIR                 = 0

    STONE               = 1

    GRASS               = 2

    DIRT                = 3

    COBBLESTONE         = 4

    WOOD_PLANKS         = 5

    SAPLING             = 6

    BEDROCK             = 7

    WATER_FLOWING       = 8

    WATER               = WATER_FLOWING

    WATER_STATIONARY    = 9

    LAVA_FLOWING        = 10

    LAVA                = LAVA_FLOWING

    LAVA_STATIONARY     = 11

    SAND                = 12

    GRAVEL              = 13

    GOLD_ORE            = 14

    IRON_ORE            = 15

    COAL_ORE            = 16

    WOOD                = 17

    LEAVES              = 18

    GLASS               = 20

    LAPIS_LAZULI_ORE    = 21

    LAPIS_LAZULI_BLOCK  = 22

    SANDSTONE           = 24

    BED                 = 26

    COBWEB              = 30

    GRASS_TALL          = 31

    WOOL                = 35

    FLOWER_YELLOW       = 37

    FLOWER_CYAN         = 38

    MUSHROOM_BROWN      = 39

    MUSHROOM_RED        = 40

    GOLD_BLOCK          = 41

    IRON_BLOCK          = 42

    STONE_SLAB_DOUBLE   = 43

    STONE_SLAB          = 44

    BRICK_BLOCK         = 45

    TNT                 = 46

    BOOKSHELF           = 47

    MOSS_STONE          = 48

    OBSIDIAN            = 49

    TORCH               = 50

    FIRE                = 51

    STAIRS_WOOD         = 53

    CHEST               = 54

    DIAMOND_ORE         = 56

    DIAMOND_BLOCK       = 57

    CRAFTING_TABLE      = 58

    FARMLAND            = 60

    FURNACE_INACTIVE    = 61

    FURNACE_ACTIVE      = 62

    DOOR_WOOD           = 64

    LADDER              = 65

    STAIRS_COBBLESTONE  = 67

    DOOR_IRON           = 71

    REDSTONE_ORE        = 73

    SNOW                = 78

    ICE                 = 79

    SNOW_BLOCK          = 80

    CACTUS              = 81

    CLAY                = 82

    SUGAR_CANE          = 83

    FENCE               = 85

    GLOWSTONE_BLOCK     = 89

    BEDROCK_INVISIBLE   = 95

    STONE_BRICK         = 98

    GLASS_PANE          = 102

    MELON               = 103

    FENCE_GATE          = 107

    GLOWING_OBSIDIAN    = 246

    NETHER_REACTOR_CORE = 247


.. _block-data:

Eiginleikar blokka
---------------------------------

"The data (or sub-type) of a block"

Data Values of blocks:
WOOL:
0: White
1: Orange
2: Magenta
3: Light Blue
4: Yellow
5: Lime
6: Pink
7: Grey
8: Light grey
9: Cyan
10: Purple
11: Blue
12: Brown
13: Green
14: Red
15:Black

WOOD:
0: Oak (up/down)
1: Spruce (up/down)
2: Birch (up/down)
(below not on Pi)
3: Jungle (up/down)
4: Oak (east/west)
5: Spruce (east/west)
6: Birch (east/west)
7: Jungle (east/west)
8: Oak (north/south)
9: Spruce (north/south)
10: Birch (north/south)
11: Jungle (north/south)
12: Oak (only bark)
13: Spruce (only bark)
14: Birch (only bark)
15: Jungle (only bark)

WOOD_PLANKS (Not on Pi):
0: Oak
1: Spruce
2: Birch
3: Jungle

SAPLING:
0: Oak
1: Spruce
2: Birch
3: Jungle (Not on Pi)

GRASS_TALL:
0: Shrub
1: Grass
2: Fern
3: Grass (color affected by biome) (Not on Pi)

TORCH:
1: Pointing east
2: Pointing west
3: Pointing south
4: Pointing north
5: Facing up

STONE_BRICK:
0: Stone brick
1: Mossy stone brick
2: Cracked stone brick
3: Chiseled stone brick

STONE_SLAB / STONE_SLAB_DOUBLE:
0: Stone
1: Sandstone
2: Wooden
3: Cobblestone
4: Brick
5: Stone Brick
Below - not on Pi
6: Nether Brick
7: Quartz

Not on Pi
SNOW_BLOCK:
0-7: Height of snow, 0 being the lowest, 7 being the highest.

TNT:
0: Inactive
1: Ready to explode

LEAVES:
1: Oak leaves
2: Spruce leaves
3: Birch leaves

SANDSTONE:
0: Sandstone
1: Chiseled sandstone
2: Smooth sandstone

STAIRS_[COBBLESTONE, WOOD]:
0: Ascending east
1: Ascending west
2: Ascending south
3: Ascending north
4: Ascending east (upside down)
5: Ascending west (upside down)
6: Ascending south (upside down)
7: Ascending north (upside down)

LADDERS, CHESTS, FURNACES, FENCE_GATE:
2: Facing north
3: Facing south
4: Facing west
5: Facing east

[WATER, LAVA]_STATIONARY:
0-7: Level of the water, 0 being the highest, 7 the lowest

NETHER_REACTOR_CORE:
0: Unused
1: Active
2: Stopped / used up    