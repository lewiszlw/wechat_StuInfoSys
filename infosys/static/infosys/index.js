function startTime()
        {
            var today=new Date()
            var year=today.getFullYear();
            var month=today.getMonth() + 1;
            var date=today.getDate();
            var day=today.getDay();
            var dayStr='';
            var h=today.getHours();
            var m=today.getMinutes();
            var s=today.getSeconds()
            // 鍦ㄥ皬浜�10鐨勬暟瀛楀墠闈㈠姞鈥�0鈥�;
            month=checkTime(month);
            date=checkTime(date);
            m=checkTime(m);
            s=checkTime(s);
            //灏嗛樋鎷変集鏁板瓧杞崲涓轰腑鏂囨暟瀛�
            dayStr = changeNumToChinese(day);
            document.getElementById('ttime').innerHTML=h+":"+m+":"+s;
            document.getElementById('ddate').innerHTML=year+"-"+month+"-"+date;
            document.getElementById('dday').innerHTML=dayStr;
            t=setTimeout('startTime()',1000);
        }
        function checkTime(i)
        {
            if (i<10) 
            {i="0" + i;}
            return i
        }
        function changeNumToChinese(j)
        {
            var dayStr = '';//杈撳嚭鐨勪腑鏂囨暟瀛�
            if(parseInt(j) == 1) { dayStr = "涓€"; }
            else if(parseInt(j) == 2) { dayStr = "浜�"; }
            else if(parseInt(j) == 3) { dayStr = "涓�"; }
            else if(parseInt(j) == 4) { dayStr = "鍥�"; }
            else if(parseInt(j) == 5) { dayStr = "浜�"; }
            else if(parseInt(j) == 5) { dayStr = "鍏�"; }
            else { dayStr = "鏃�"; } 
            return dayStr;                       
        }
