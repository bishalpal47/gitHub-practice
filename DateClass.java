package encapsulation;

public class DateClass {
    private int day;
    private int month;
    private int year;  

    public int getDay() {
        return day;
    }

    public void setDay(int day) {
        if(day <= 0 || day > 31) {
            day = 1;        // making the correction.
        }
        this.day = day;
    }

    public int getMonth() {
        return month;
    }

    public void setMonth(int month) {
        if(month <= 0) {
            month = 1;
        }
        else if(month > 12) {
            month = month % 12;
        }
        this.month = month;
    }

    public int getYear() {
        return year;
    }

    public void setYear(int year) {
        if(year < 0) {
            year = 0;
        }
        this.year = year;
    }



    public String getNameOfMonth(int m) {
        String monthName = "";
        if(m == 0) {
            m = 1;
        }
        switch (m) {
            case 1 : monthName = "January";
            break;
            case 2 : monthName = "February";
            break;
            case 3 : monthName = "March";
                break;
            case 4 : monthName = "April";
                break;
            case 5 : monthName = "May";
                break;
            case 6 : monthName = "June";
                break;
            case 7 : monthName = "July";
                break;
            case 8 : monthName = "August";
                break;
            case 9 : monthName = "Septemeber";
                break;
            case 10 : monthName = "October";
                break;
            case 11 : monthName = "November";
                break;
            case 12 : monthName = "December";
                break;
        }
        return monthName;
    }

    public String getDate() {
        StringBuilder theDate = new StringBuilder();
        // day month year       23 November 2024      "23 November 2024"
        theDate.append(this.getDay());
        theDate.append(" ");
        theDate.append(this.getNameOfMonth(this.getMonth()));
        theDate.append(" ");
        theDate.append(this.getYear());
        return theDate.toString();
    }

    public static void main(String[] args) {
        DateClass obj1 = new DateClass();
        obj1.setDay(60);
        obj1.setMonth(15);
        obj1.setYear(-1254);

        System.out.println(obj1.getDate());

        DateClass obj2 = new DateClass();
        obj2.setDay(22);
        obj2.setMonth(9);
        obj2.setYear(2005);
        System.out.println("birthday - " + obj2.getDate());
    }
}
