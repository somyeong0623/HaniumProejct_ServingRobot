kprice1=7000;
kprice2=8000;
kprice3=6500;
kprice4=6500;
cprice1=7000;
cprice2=7000;
cprice3=8000;
cprice4=7000;
aprice1=8000;
aprice2=9000;
aprice3=8000;
aprice4=10000;
jprice1=8000;
jprice2=7000;
jprice3=7000;
jprice4=8000;

let kname1="전주비빔밥"
let kname2

function listing() {
    $.ajax({
        type: "GET",
        url: "/pos?sample_give=샘플데이터",
        data: {},
        success: function (response) {
            alert(response['msg'])
        }
    })
}

function add1() {
	let name=kname1
	// price=kprice1;
	let count=kcount1;
	console.log(name, count)

    // $.ajax({
    //     type: "POST",
    //     url: "/pos",
    //     data: {sample_give: '샘플데이터'},
    //     success: function (response) {
    //         alert(response['msg'])
    //     }
    // })
}
