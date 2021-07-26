// kprice1=7000;
// kprice2=8000;
// kprice3=6500;
// kprice4=6500;
// cprice1=7000;
// cprice2=7000;
// cprice3=8000;
// cprice4=7000;
// aprice1=8000;
// aprice2=9000;
// aprice3=8000;
// aprice4=10000;
// jprice1=8000;
// jprice2=7000;
// jprice3=7000;
// jprice4=8000;
//
// let kname1="전주비빔밥"
// let kname2
//
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
//
// function add1() {
// 	let name=kname1
// 	let count=kcount1;
// 	if(count==1) {
//         console.log(name, count)
//
//         $.ajax({
//             type: "POST",
//             url: "/add1",
//             data: {name_give:name, count_give:count},
//             success: function (response) {
//                 alert(response['msg'])
//             }
//         })
//
//     }
// }

function payment() {

    $('#menu_list tr').each(function () {
        var tr = $(this);
        var td = tr.children();
        let menu_name=td.find('.menu_name').text();
        let menu_count=td.find('.menu_count').text();
        console.log(menu_name, menu_count);
    });

}