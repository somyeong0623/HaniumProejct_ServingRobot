//[메뉴 고르러가기]버튼 눌렀을때
//테이블번호, 전화번호 저장해노 놓고, 메뉴 고르면
//한번에 db로 insert

$(document).ready(function () {
    listing()
})
    function listing() {
    $.ajax({
        type: "GET",
        url: "/order?sample_give=샘플데이터",
        data: {},
        success: function (response) {
            alert(response['msg'])
        }
    })
}

function go_order() {
    $.ajax({
    type: "POST",
    url: "/order",
    data: { sample_give:'샘플데이터' },
    success: function(response){
        alert(response['msg'])
    }
  })
    // let table_number = $('#table_number').val()
    // let phone_number = $('#phone_number').val()
    // alert('안녕!!!')
    // console.log(table_number, phone_number);


}
