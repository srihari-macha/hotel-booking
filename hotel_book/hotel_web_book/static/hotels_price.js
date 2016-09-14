/**
 * Created by cfit008 on 14/9/16.
 */
 $(document).ready(function () {

     $.ajax({
         type: 'POST',
         url: 'hotel_price_home',
         headers: {
             add_contid: 'asdfg123',
             token: 'qwerty123yuiop'
         },



         success: function (data) {
             $('#msg_add').text(data);

         }
     });
 });