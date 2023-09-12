package com.example.proj1;

import androidx.appcompat.app.AppCompatActivity;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;

import org.w3c.dom.Text;

import java.util.Random;

public class hardModeQuestions extends AppCompatActivity {
    private static LineGraphSeries<DataPoint> series;
    private static int number;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_hard_mode_questions);
        GraphView graph = (GraphView) findViewById(R.id.graph);
        TextView question = (TextView) findViewById(R.id.question);
        Button submit = (Button) findViewById(R.id.Submit);
        EditText solution = (EditText) findViewById(R.id.userInput);
        TextView output = (TextView) findViewById(R.id.output);
        Random rand = new Random();
        int number = rand.nextInt(6);
        double x, y;
        if (number == 1) {
            question = (TextView) findViewById(R.id.question);
            question.setText("Find Integral between the following y bounds in the graph y = x^5 + x: -10 and 5");
            x = -5.0;
            graph = (GraphView) findViewById(R.id.graph);
            series = new LineGraphSeries<DataPoint>();
            series.setDrawBackground(true);
            series.setBackgroundColor(Color.GREEN);
            y = 0;
            for (int i = -10; i < 5; i++) {
                x = x + 1;
                y = Math.pow(x, 5) + Math.pow(x, 1);
                series.appendData(new DataPoint(x, y), true, 500);
            }
            graph.addSeries(series);
            submit.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (solution.getText().toString().equals("164100")) {
                        output.setText("Correct");
                    } else {
                        output.setText("Wrong");
                    }
                }
            });
        } else if (number == 2) {
            question.setText("Find Integral between the following bounds in the graph y = x^3 + x: -5 and 12");
            x = -5.0;
            graph = (GraphView) findViewById(R.id.graph);
            series = new LineGraphSeries<DataPoint>();
            series.setDrawBackground(true);
            series.setBackgroundColor(Color.GREEN);
            y = 0;
            for (int i = -5; i < 12; i++) {
                x = x + 1;
                y = Math.pow(x, 3) + Math.pow(x, 1);
                series.appendData(new DataPoint(x, y), true, 500);
            }
            graph.addSeries(series);
            submit.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (solution.getText().toString().equals("5087.25")) {
                        output.setText("Correct");
                    } else {
                        output.setText("Wrong");
                    }
                }
            });
        } else if (number == 4) {
            question = (TextView) findViewById(R.id.question);
            question.setText("Find Integral between the following y bounds in the graph y = x^7 + x^5 + x: -5 and 7");
            x = -5.0;
            series = new LineGraphSeries<DataPoint>();
            series.setDrawBackground(true);
            series.setBackgroundColor(Color.GREEN);
            y = 0;
            for (int i = -5; i < 7; i++) {
                x = x + 1;
                y = Math.pow(x, 7) + Math.pow(x, 5) + Math.pow(x, 1);
                series.appendData(new DataPoint(x, y), true, 500);
            }
            graph.addSeries(series);
            submit.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (solution.getText().toString().equals("688788")) {
                        output.setText("Correct");
                    } else {
                        output.setText("Wrong");
                    }
                }
            });
        } else if (number == 5) {
            question = (TextView) findViewById(R.id.question);
            question.setText("Find Integral between the following y bounds in the graph y = x^10 + x^7: 4 and 7");
            x = -5.0;
            series = new LineGraphSeries<DataPoint>();
            series.setDrawBackground(true);
            series.setBackgroundColor(Color.GREEN);
            y = 0;
            for (int i = 4; i < 7; i++) {
                x = x + 1;
                y = Math.pow(x, 10) + Math.pow(x, 7);
                series.appendData(new DataPoint(x, y), true, 500);
            }
            graph.addSeries(series);
            submit.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (solution.getText().toString().equals("180088084.4")) {
                        output.setText("Correct");
                    } else {
                        output.setText("Wrong");
                    }
                }
            });
        } else {
            question = (TextView) findViewById(R.id.question);
            question.setText("Find Integral between the following y bounds in the graph y = x^6 + x^7 + x^2: 4 and 13");
            x = -5.0;
            series = new LineGraphSeries<DataPoint>();
            series.setDrawBackground(true);
            series.setBackgroundColor(Color.GREEN);
            y = 0;
            for (int i = 4; i < 7; i++) {
                x = x + 1;
                y = Math.pow(x, 6) + Math.pow(x, 7) + Math.pow(x, 2);
                series.appendData(new DataPoint(x, y), true, 500);
            }
            graph.addSeries(series);
            submit.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    if (solution.getText().toString().equals("110920592.4")) {
                        output.setText("Correct");
                    } else {
                        output.setText("Wrong");
                    }
                }
            });}

            Button nextButton1 = (Button) findViewById(R.id.next);
            nextButton1.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    Intent intent = getIntent();
                    finish();
                    startActivity(intent);
                }
            });
        }


    }