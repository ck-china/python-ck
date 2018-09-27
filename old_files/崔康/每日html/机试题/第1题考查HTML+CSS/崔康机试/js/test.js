$(function(){
	$('#btn').click(function(){
				var txt1 = $('#name').val();
				$('#name').val('');
				var txt2 = $('#email').val();
				$('#email').val('');
				var txt3 = $('#salary').val();
				$('#salary').val('');

				if(txt1 == ''){
					alert('请输入内容！');
					return;
				}
				var $li = $("<li>"+txt1+" "+txt2+" "+txt3+" <a href='javascript:;'' class='del'>delate</a>"+"</li>"+"<br>")
				//把li添加到ul中
				$li.appendTo('#list');
			});
	/*$('#list').delegate('a','click',function(){
				var handler = $(this).attr('class');
				switch(handler){
					case 'del':
						var txt = $(this).parent().children(':first').html();
						if(confirm('你确定要删除"'+txt+'"吗？')){
							$(this).parent().remove();
						}
						break;
					}
				}*/
})