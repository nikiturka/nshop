$(document).ready(function(){

    var button_add = $('.plus');
    var cart_ul = $('.cart-ul');

    function cartUpdate(id, quantity, is_delete){

        var form = $('.quantity-form');
        var url = $('.url').data('url');
        var name = button_add.data('name');

        if(is_delete == true){
            var data = {
                'id': id,
                'quantity': quantity,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'is_delete': 'delete'
            }
             alert(name + " was removed from your cart!");
        } else{
            var data = {
                'id': id,
                'quantity': quantity,
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val(),
                'is_delete': 'not to delete'
            }
            alert(name + " was added to your cart!");
        }

        //AJAX CALL
        $.ajax({
            url: url,
            type: 'POST',
            data: data,
            success: function(data){
                location.reload(true);
            }
        })

    }

    //CART SHOW
    $('.cart-word').on("click", function(e){
        e.preventDefault();
        var cart = $('.element');
        var count = $('.li-element').length;
        if( cart.is(":hidden") && count != 0){
            cart.removeAttr('hidden');
        } else{
            $('.element').attr('hidden', true);
        }
    })

    //CART ADD
    button_add.on('click', function(e){
        e.preventDefault();

        var quantity = $('.quantity').val();
        var id = button_add.data('id');
        var token = $('input[name=csrfmiddlewaretoken]').val();

        cartUpdate(id, quantity, is_delete=false);

    })

    //CART REMOVE
    $('.remove').on('click', function(e){
        e.preventDefault();

        var quantity = $('.quantity').val();
        var id = $(this).data('id');
        var token = $('input[name=csrfmiddlewaretoken]').val();

        cartUpdate(id, quantity, is_delete=true);
    })

    //CART TOTAL PRICE COUNT (Doesn't work now)
    var total_order_price = 0;
    $(".total").each(function(){
        total_order_price += parseInt($(this).text());
    });
    if(total_order_price > 0){
        $(".total-price").text("Total price: " + total_order_price + " €");
    }

    //TOAST
    var option = {
        animation: true,
        delay: 2000
    };

    $('.buy-form').on('submit', function(){
        alert('Your order was received, we will call you soon. Stay in touch!');
    })
});
