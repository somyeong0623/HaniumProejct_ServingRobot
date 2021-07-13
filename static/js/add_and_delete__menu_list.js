let total_price=0;

let kcount1=0;
let kprice1=0;
let kprice1_total=0;
function add_kfood1(){
		let menu_image=$('#kimage1').attr('src');
    	let menu_name=$('#kname1').text();
    	let menu_price=$('#kprice1').text()
    	let temp_html = `<tr id="bibimbap">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="kminus1()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="kcount1" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="kplus1()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_kfood1()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(kcount1==0) {
		$('#menu_list').append(temp_html);
		kcount1=kcount1+1;
		kprice1=parseInt(menu_price);
		kprice1_total=kprice1;
		total_price+=kprice1;
		$('#total_price').text(total_price);
	}

}
function delete_kfood1() {
        $('#bibimbap').remove();
        kcount1=kcount1-1;
        kkcount1=1;
        total_price-=kprice1_total;
        $('#total_price').text(total_price);
    }

let kcount2=0;
let kprice2;
let kprice2_total=0;
function add_kfood2(){
		let menu_image=$('#kimage2').attr('src');
    	let menu_name=$('#kname2').text();
    	let menu_price=$('#kprice2').text();
    	let temp_html = `<tr id="bulgogi">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="kminus2()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="kcount2" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="kplus2()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_kfood2()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(kcount2==0) {
		$('#menu_list').append(temp_html);
		kcount2=kcount2+1;
		kprice2=parseInt(menu_price);
		kprice2_total=kprice2;
		total_price+=kprice2;
		$('#total_price').text(total_price);
	}

}
function delete_kfood2() {
        $('#bulgogi').remove();
        kcount2=kcount2-1;
        kkcount2=1;
         total_price-=kprice2_total;
        $('#total_price').text(total_price);
    }

let kcount3=0;
let kprice3;
let kprice3_total=0;
function add_kfood3(){
		let menu_image=$('#kimage3').attr('src');
    	let menu_name=$('#kname3').text();
    	let menu_price=$('#kprice3').text();
    	let temp_html = `<tr id="kimchi_stew">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="kminus3()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="kcount3" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="kplus3()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_kfood3()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(kcount3==0) {
		$('#menu_list').append(temp_html);
		kcount3=kcount3+1;
		kprice3=parseInt(menu_price);
		kprice3_total=kprice3;
		total_price+=kprice3;
		$('#total_price').text(total_price);
	}
}
function delete_kfood3() {
        $('#kimchi_stew').remove();
        kcount3=kcount3-1;
        kkcount3=1;
        total_price-=kprice3_total;
        $('#total_price').text(total_price);
    }

let kcount4=0;
let kprice4;
let kprice4_total=0;
function add_kfood4(){
		let menu_image=$('#kimage4').attr('src');
    	let menu_name=$('#kname4').text();
    	let menu_price=$('#kprice4').text();
    	let temp_html = `<tr id="Soybean_Paste_Stew">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="kminus4()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="kcount4" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="kplus4()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_kfood4()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(kcount4==0) {
		$('#menu_list').append(temp_html);
		kcount4=kcount4+1;
		kprice4=parseInt(menu_price);
		kprice4_total=kprice4;
		total_price+=kprice4;
		$('#total_price').text(total_price);
	}
}
function delete_kfood4() {
        $('#Soybean_Paste_Stew').remove();
        kcount4=kcount4-1;
        kkcount4=1;
        total_price-=kprice4_total;
        $('#total_price').text(total_price);
    }

let ccount1=0;
let cprice1;
let cprice1_total=0;
function add_cfood1(){
		let menu_image=$('#cimage1').attr('src');
    	let menu_name=$('#cname1').text();
    	let menu_price=$('#cprice1').text();
    	let temp_html = `<tr id="Jajangmyeon">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="cminus1()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="ccount1" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="cplus1()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_cfood1()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(ccount1==0) {
		$('#menu_list').append(temp_html);
		ccount1=ccount1+1;
		cprice1=parseInt(menu_price);
		cprice1_total=cprice1;
		total_price+=cprice1;
		$('#total_price').text(total_price);
	}
}
function delete_cfood1() {
        $('#Jajangmyeon').remove();
        ccount1=ccount1-1;
        cccount1=1;
        total_price-=cprice1_total;
        $('#total_price').text(total_price);
    }

let ccount2=0;
let cprice2;
let cprice2_total=0;
function add_cfood2(){
		let menu_image=$('#cimage2').attr('src');
    	let menu_name=$('#cname2').text();
    	let menu_price=$('#cprice2').text();
    	let temp_html = `<tr id="jjamppong">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="cminus2()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="ccount2" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="cplus2()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_cfood2()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(ccount2==0) {
		$('#menu_list').append(temp_html);
		ccount2=ccount2+1;
		cprice2=parseInt(menu_price);
		cprice2_total=cprice2;
		total_price+=cprice2;
		$('#total_price').text(total_price);
	}
}
function delete_cfood2() {
        $('#jjamppong').remove();
        ccount2=ccount2-1;
        cccount2=1;
        total_price-=cprice2_total;
        $('#total_price').text(total_price);
    }

let ccount3=0;
let cprice3;
let cprice3_total=0;
function add_cfood3(){
		let menu_image=$('#cimage3').attr('src');
    	let menu_name=$('#cname3').text();
    	let menu_price=$('#cprice3').text();
    	let temp_html = `<tr id="Sweet_and_sour_pork">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="cminus3()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="ccount3" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="cplus3()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_cfood3()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(ccount3==0) {
		$('#menu_list').append(temp_html);
		ccount3=ccount3+1;
		cprice3=parseInt(menu_price);
		cprice3_total=cprice3;
		total_price+=cprice3;
		$('#total_price').text(total_price);
	}
}
function delete_cfood3() {
        $('#Sweet_and_sour_pork').remove();
        ccount3=ccount3-1;
        cccount3=1;
        total_price-=cprice3_total;
        $('#total_price').text(total_price);
    }

let ccount4=0;
let cprice4;
let cprice4_total=0;
function add_cfood4(){
		let menu_image=$('#cimage4').attr('src');
    	let menu_name=$('#cname4').text();
    	let menu_price=$('#cprice4').text();
    	let temp_html = `<tr id="fried_rice">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="cminus4()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="ccount4" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="cplus4()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_cfood4()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(ccount4==0) {
		$('#menu_list').append(temp_html);
		ccount4=ccount4+1;
		cprice4=parseInt(menu_price);
		cprice4_total=cprice4;
		total_price+=cprice4;
		$('#total_price').text(total_price);
	}
}
function delete_cfood4() {
        $('#fried_rice').remove();
        ccount4=ccount4-1;
        cccount4=1;
        total_price-=cprice4_total;
        $('#total_price').text(total_price);
    }

let acount1=0;
let aprice1;
let aprice1_total=0;
function add_afood1(){
		let menu_image=$('#aimage1').attr('src');
    	let menu_name=$('#aname1').text();
    	let menu_price=$('#aprice1').text();
    	let temp_html = `<tr id="tomato_pasta">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="aminus1()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="acount1" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="aplus1()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_afood1()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(acount1==0) {
		$('#menu_list').append(temp_html);
		acount1=acount1+1;
		aprice1=parseInt(menu_price);
		aprice1_total=aprice1;
		total_price+=aprice1;
		$('#total_price').text(total_price);
	}
}
function delete_afood1() {
        $('#tomato_pasta').remove();
        acount1=acount1-1;
        aacount1=1;
        total_price-=aprice1_total;
        $('#total_price').text(total_price);
    }

let acount2=0;
let aprice2;
let aprice2_total=0;
function add_afood2(){
		let menu_image=$('#aimage2').attr('src');
    	let menu_name=$('#aname2').text();
    	let menu_price=$('#aprice2').text();
    	let temp_html = `<tr id="Hamburg_Steak">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="aminus2()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="acount2" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="aplus2()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_afood2()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(acount2==0) {
		$('#menu_list').append(temp_html);
		acount2=acount2+1;
		aprice2=parseInt(menu_price);
		aprice2_total=aprice2;
		total_price+=aprice2;
		$('#total_price').text(total_price);
	}
}
function delete_afood2() {
        $('#Hamburg_Steak').remove();
        acount2=acount2-1;
        aacount2=1;
        total_price-=aprice2_total;
        $('#total_price').text(total_price);
    }

let acount3=0;
let aprice3;
let aprice3_total=0;
function add_afood3(){
		let menu_image=$('#aimage3').attr('src');
    	let menu_name=$('#aname3').text();
    	let menu_price=$('#aprice3').text();
    	let temp_html = `<tr id="Omurice">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="aminus3()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="acount3" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="aplus3()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_afood3()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(acount3==0) {
		$('#menu_list').append(temp_html);
		acount3=acount3+1;
		aprice3=parseInt(menu_price);
		aprice3_total=aprice3;
		total_price+=aprice3;
		$('#total_price').text(total_price);
	}
}
function delete_afood3() {
        $('#Omurice').remove();
        acount3=acount3-1;
        aacount3=1;
        total_price-=aprice3_total;
        $('#total_price').text(total_price);
    }

let acount4=0;
let aprice4;
let aprice4_total=0;
function add_afood4(){
		let menu_image=$('#aimage4').attr('src');
    	let menu_name=$('#aname4').text();
    	let menu_price=$('#aprice4').text();
    	let temp_html = `<tr id="pizza">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="aminus4()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="acount4" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="aplus4()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_afood4()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(acount4==0) {
		$('#menu_list').append(temp_html);
		acount4=acount4+1;
		aprice4=parseInt(menu_price);
		aprice4_total=aprice4;
		total_price+=aprice4;
		$('#total_price').text(total_price);
	}
}
function delete_afood4() {
        $('#pizza').remove();
        acount4=acount4-1;
        aacount4=1;
        total_price-=aprice4_total;
        $('#total_price').text(total_price);
    }

let jcount1=0;
let jprice1;
let jprice1_total=0;
function add_jfood1(){
		let menu_image=$('#jimage1').attr('src');
    	let menu_name=$('#jname1').text();
    	let menu_price=$('#jprice1').text();
    	let temp_html = `<tr id="pork_cutlet">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="jminus1()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="jcount1" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="jplus1()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_jfood1()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(jcount1==0) {
		$('#menu_list').append(temp_html);
		jcount1=jcount1+1;
		jprice1=parseInt(menu_price);
		jprice1_total=jprice1;
		total_price+=jprice1;
		$('#total_price').text(total_price);
	}
}
function delete_jfood1() {
        $('#pork_cutlet').remove();
        jcount1=jcount1-1;
        jjcount1=1;
        total_price-=jprice1_total;
        $('#total_price').text(total_price);
    }

let jcount2=0;
let jprice2;
let jprice2_total=0;
function add_jfood2(){
		let menu_image=$('#jimage2').attr('src');
    	let menu_name=$('#jname2').text();
    	let menu_price=$('#jprice2').text();
    	let temp_html = `<tr id="Okonomiyaki">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="jminus2()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="jcount2" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="jplus2()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_jfood2()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(jcount2==0) {
		$('#menu_list').append(temp_html);
		jcount2=jcount2+1;
		jprice2=parseInt(menu_price);
		jprice2_total=jprice2;
		total_price+=jprice2;
		$('#total_price').text(total_price);
	}
}
function delete_jfood2() {
        $('#Okonomiyaki').remove();
        jcount2=jcount2-1;
        jjcount2=1;
        total_price-=jprice2_total;
        $('#total_price').text(total_price);
    }

let jcount3=0;
let jprice3;
let jprice3_total=0;
function add_jfood3(){
		let menu_image=$('#jimage3').attr('src');
    	let menu_name=$('#jname3').text();
    	let menu_price=$('#jprice3').text();
    	let temp_html = `<tr id="Katsudon">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="jminus3()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="jcount3" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="jplus3()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_jfood3()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(jcount3==0) {
		$('#menu_list').append(temp_html);
		jcount3=jcount3+1;
		jprice3=parseInt(menu_price);
		jprice3_total=jprice3;
		total_price+=jprice3;
		$('#total_price').text(total_price);
	}
}
function delete_jfood3() {
        $('#Katsudon').remove();
        jcount3=jcount3-1;
        jjcount3=1;
        total_price-=jprice3_total;
        $('#total_price').text(total_price);
    }

let jcount4=0;
let jprice4;
let jprice4_total=0;
function add_jfood4(){
		let menu_image=$('#jimage4').attr('src');
    	let menu_name=$('#jname4').text();
    	let menu_price=$('#jprice4').text();
    	let temp_html = `<tr id="sushi">
\t<td>
<figure class="media">
\t<div class="img-wrap"><img src="${menu_image}" class="img-thumbnail img-xs"></div>
\t<figcaption class="media-body">
\t\t<h6 class="title text-truncate">${menu_name} </h6>
\t</figcaption>
</figure>
\t</td>
\t<td class="text-center">
\t\t<div class="m-btn-group m-btn-group--pill btn-group mr-2" role="group" aria-label="...">
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="jminus4()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-minus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button id="jcount4" type="button"
                                                                                class="m-btn btn btn-default count-color"
                                                                                disabled>1</button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t<button onclick="jplus4()" type="button"
                                                                                class="m-btn btn btn-default"><i
                                                                                class="fa fa-plus"></i></button>
\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t</div>
\t</td>
\t<td>
\t\t<div class="price-wrap">
\t\t\t<var class="price">${menu_price}</var>
\t\t</div> <!-- price-wrap .// -->
\t</td>
\t<td class="text-right">
\t<button onclick="delete_jfood4()" type="button" class="btn btn-outline-danger"> <i class="fa fa-trash"></i></button>
\t</td>
</tr>`
	if(jcount4==0) {
		$('#menu_list').append(temp_html);
		jcount4=jcount4+1;
		jprice4=parseInt(menu_price);
		jprice4_total=jprice4;
		total_price+=jprice4;
		$('#total_price').text(total_price);
	}
}
function delete_jfood4() {
        $('#sushi').remove();
        jcount4=jcount4-1;
        jjcount4=1;
        total_price-=jprice4_total;
        $('#total_price').text(total_price);
    }