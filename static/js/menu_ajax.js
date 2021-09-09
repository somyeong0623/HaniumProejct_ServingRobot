// 결제 완료버튼을 누를시 장바구니(포스창 오른쪽의 주문내역)에서
// 메뉴리스트의 메뉴이름, 메뉴 수량을 받아와서 데이터베이스에 삽입
// 이때, initial page에서 넘겨받은 table_no과, o_id를 기준으로 해당 doc의 menu리스트에 값을 추가한다.

// function listing() {
//     $.ajax({
//         type: "GET",
//         url: "/pos?sample_give=샘플데이터",
//         data: {},
//         success: function (response) {
//             alert(response['msg'])
//         }
//     })
// }
function GetURLParameter(sParam)
{
    var sPageURL = window.location.search.substring(1);
    var sURLVariables = sPageURL.split('&');
    for (var i = 0; i < sURLVariables.length; i++)
    {
        var sParameterName = sURLVariables[i].split('=');
        if (sParameterName[0] == sParam)
        {
            return sParameterName[1];
        }
    }
}
//
var table_no = GetURLParameter('table_number');
var o_id=GetURLParameter('o_id')
// var table_no = getUrlVars();

// 결제내역 Order테이블에 삽입
// table_no에 해당하는 값 Robot table에서 sig 1->0으로 변경

function payment() {
    console.log("payment() 함수 실행!!!")
    let list = [];
    $('#menu_list tr').each(function () {
        var tr = $(this);
        var td = tr.children();
        let menu_name = td.find('.menu_name').text();
        menu_name=menu_name.replace(" ","")
        let menu_id=0;
        if(menu_name=="전주비빔밥") {
            menu_id =0;
        }else if(menu_name=="뚝배기불고기"){
            menu_id=1;
        }else if(menu_name=="김치찌개"){
            menu_id=2;
        }else if(menu_name=="된장찌개"){
            menu_id=3;
        }else if(menu_name=="짜장면"){
            menu_id=4;
        }else if(menu_name=="짬뽕"){
            menu_id=5;
        }else if(menu_name=="탕수육"){
            menu_id=6;
        }
        else if(menu_name=="볶음밥"){
            menu_id=7;
        }
        else if(menu_name=="토마토파스타"){
            menu_id=8;
        }
        else if(menu_name=="함박스테이크"){
            menu_id=9;
        }
        else if(menu_name=="오므라이스"){
            menu_id=10;
        }else if(menu_name=="페퍼로니피자"){
            menu_id=11;
        }else if(menu_name=="등심돈까스"){
            menu_id=12;
        }else if(menu_name=="오코노미야끼"){
            menu_id=13;
        }else if(menu_name=="가츠동"){
            menu_id=14;
        }
        else if(menu_name=="모듬초밥(10p)"){
            menu_id=15;
        }





        let menu_count = td.find('.menu_count').text();
        console.log(menu_id,menu_name, menu_count);
        list.push({"id": menu_id,"name": menu_name,"count": menu_count});
    });
    let total_price=$('#total_price').text();
    console.log("table_no: "+table_no, "o_id: "+o_id ,"total_price: ",total_price);
    console.log(list);
    var data = JSON.stringify({menulist_give: list, o_id_give:o_id, total_price_give:total_price});

    $.ajax({
        type: "POST",
        url: "/menu",
        contentType: "application/json",
        data: data,
        success: function (response) {
        }
    })

}