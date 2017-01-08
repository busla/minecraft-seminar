.. _verkefni16:

Verkefni 16
===========

Í síðasta verkefni vorum við að senda skilaboð í Minecraft. Þið tókuð kannski eftir því að það var ekki hægt að athuga hvort þú værir strákur eða stelpa svo við gætum skrifað *komin* fyrir bæði kyn.

Við getum athugað það með því að spyrja forritið okkar hvort þú sért strákur eða stelpa og svo prenta út það sem á við.

*Dæmi*

Ef ég == kona:
    skrifaðu *komin*

Annars:
    skrifaðu *kominn*


Í forritinu ykkar myndi þetta líta svona út:


.. code-block:: python
    
    from mcpi.minecraft import Minecraft
    from datetime import datetime
    import time

    mc = Minecraft.create()

    nafn = input('Skrifaðu nafnið þitt: ')
    svar = input('Hvaða kyn ertu? (kk/kvk): ')

    if svar == 'kk':
        mc.postToChat('hann ' + nafn + ' er kominn inn!')

    else:
        mc.postToChat('hun ' + nafn + ' er komin inn!')

    while True:
        skilabod = input('Skilaboð: ')

        if skilabod == '':
            print('Þú skrifaðir engan texta, prófaðu aftur!')
        else:
            mc.postToChat(nafn + ": " + skilabod)
