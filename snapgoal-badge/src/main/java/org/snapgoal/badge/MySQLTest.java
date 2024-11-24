package org.snapgoal.badge;

import java.sql.Connection;
import java.sql.DriverManager;

public class MySQLTest {
    public static void main(String[] args) {
        try {
            Class.forName("com.mysql.cj.jdbc.Driver"); // Load the driver
            Connection conn = DriverManager.getConnection(
                "jdbc:mysql://localhost:3306/snapgoal",
                "user",
                "password123"
            );
            System.out.println("Connection Successful!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

