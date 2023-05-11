function showproductid(productid){
    const count = $('#count').val();
    $.get('/orders/add_to_order?product_id=' + productid + '&count=' + count
        ).then(res=>{
            Swal.fire({
  title: 'اعلان',
  text: res.text,
  icon: res.icon,
  showCancelButton: false,
  confirmButtonColor: '#3085d6',
  cancelButtonColor: '#d33',
  confirmButtonText: res.confirmButtonText
})
    })
}

function calc(product_id){
    $.get('/user/cart/remove', {
        id:product_id
    }).then(location.reload())

}

function test(articleid) {
    var comment = $("#commentText").val();
    $.get('/blogs/add-article-comment', {
        article_comment:comment,
        article_id:articleid
    }).then(location.reload())
}

function change_count(product_id,operation){
    $.get('/user/cart/amount',{
        id:product_id,
        op:operation,
    }).then(location.reload())

}

