Verkefni 12
===========

Allar tölur á milli

.. code-block:: javascript
    
    function AllarTolurAMilli(a, b){
        var listi = [];
        for(var i = a + 1; i < b ; i++){
            listi.push(i);
        }
        return listi;
    }
    
    var millibil = AllarTolurAMilli(5, 19);

    console.log(millibil);

