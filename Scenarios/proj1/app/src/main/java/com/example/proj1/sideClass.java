package com.example.proj1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;

public class sideClass {
    private static String a = "something12";
    public static void main(String[] args) {
    }
    public String output(){
        try {
            String pythonScriptPath =  "";
            ProcessBuilder pb = new ProcessBuilder("python",pythonScriptPath).inheritIO();
            Process p = pb.start();
            BufferedReader bfr = new BufferedReader(new InputStreamReader(p.getInputStream()));
            System.out.println(".........start   process.........");
            String line = "";
            a = "something";
            while ((line = bfr.readLine()) != null) {
                System.out.println("Python Output: " + line);
                a = "something";
            }

        } catch (IOException ie) {
            a = "somethingError";
            ie.printStackTrace();
        }
        return a;
    }

}
