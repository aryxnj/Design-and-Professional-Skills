package com.example.proj1;

import android.content.Intent;
import android.graphics.Color;
import android.os.Bundle;

import com.chaquo.python.PyObject;
import com.chaquo.python.Python;
import com.chaquo.python.android.AndroidPlatform;
import com.google.android.material.snackbar.Snackbar;

import androidx.appcompat.app.AppCompatActivity;

import android.text.Html;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.navigation.NavController;
import androidx.navigation.Navigation;
import androidx.navigation.ui.AppBarConfiguration;
import androidx.navigation.ui.NavigationUI;

import com.example.proj1.databinding.ActivityQuestionStyleBinding;
import com.jjoe64.graphview.GraphView;
import com.jjoe64.graphview.series.DataPoint;
import com.jjoe64.graphview.series.LineGraphSeries;
import com.example.proj1.MainActivity;

import org.w3c.dom.Text;

public class questionStyle extends AppCompatActivity {

    private AppBarConfiguration appBarConfiguration;
    private ActivityQuestionStyleBinding binding;
    private static LineGraphSeries<DataPoint> series;
    private static LineGraphSeries<DataPoint> series1;
    private static int countAddMore = 0;
    private static int minusCount = 0;
    private static String testMain = MainActivity.usernameFinal;
    private static String question;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        binding = ActivityQuestionStyleBinding.inflate(getLayoutInflater());
        setContentView(binding.getRoot());

        setSupportActionBar(binding.toolbar);

        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_content_question_style);
        appBarConfiguration = new AppBarConfiguration.Builder(navController.getGraph()).build();
        NavigationUI.setupActionBarWithNavController(this, navController, appBarConfiguration);

        binding.fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
        double x,y;
        x = -5.0;
        GraphView graph = (GraphView) findViewById(R.id.graph);
        series = new LineGraphSeries<DataPoint>();
        series.setDrawBackground(true);
        series.setBackgroundColor(Color.GREEN);
        for (int i = -5; i < 5; i++){
            x = x + 1;
            y = Math.pow(x, 2);
            series.appendData(new DataPoint(x,y), true, 500);
        }
        graph.addSeries(series);
        TextView questionText = (TextView) findViewById(R.id.questionText);
        if(!Python.isStarted()){
            Python.start(new AndroidPlatform(this));
        }
        Python py = Python.getInstance();
        final PyObject pyObject = py.getModule("sampleQuestionGenerator");
        final Intent questionStyle1 = new Intent(this, questionStyle.class);
        PyObject py1 = pyObject.callAttr("run1");
        questionText.setText("Find differential of y = " + (py1.toString()));
        question = py1.toString();
//        Python py = Python.getInstance();
//        final PyObject pyObject = py.getModule("main");
//        final Intent questionStyle1 = new Intent(this, questionStyle.class);
//        PyObject py1 = pyObject.callAttr("run", "nkkm");
//        questionText.setText(py1.toString());
        Button more = (Button) findViewById(R.id.addMore);
        more.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                if (countAddMore == 0){
                    TextView add = (EditText) findViewById(R.id.add1);
                    add.setVisibility(View.VISIBLE);
                }
                else if (countAddMore == 1){
                    TextView add = (EditText) findViewById(R.id.add2);
                    add.setVisibility(View.VISIBLE);
                }
                else if (countAddMore == 2){
                    TextView add = (EditText) findViewById(R.id.add3);
                    add.setVisibility(View.VISIBLE);
                }
                else if (countAddMore == 3){
                    TextView add = (EditText) findViewById(R.id.add4);
                    add.setVisibility(View.VISIBLE);
                }
                else if (countAddMore == 4){
                    TextView add = (EditText) findViewById(R.id.add5);
                    add.setVisibility(View.VISIBLE);
                }
                else{
                    countAddMore = 0;
                }
                countAddMore ++;
            }
        });
        Button minusOne = (Button) findViewById(R.id.minusOne);
        minusOne.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                TextView add = (EditText) findViewById(R.id.add1);
                add.setVisibility(View.INVISIBLE);
                add = (EditText) findViewById(R.id.add2);
                add.setVisibility(View.INVISIBLE);
                add = (EditText) findViewById(R.id.add3);
                add.setVisibility(View.INVISIBLE);
                add = (EditText) findViewById(R.id.add4);
                add.setVisibility(View.INVISIBLE);
                add = (EditText) findViewById(R.id.add5);
                add.setVisibility(View.INVISIBLE);
                countAddMore = 0;
            }

        });
        TextView outputTest = (TextView) findViewById(R.id.outputTest);
        Button submitAnswer = (Button) findViewById(R.id.submitAnswer);
        EditText answerEntry = (EditText) findViewById(R.id.answerEntry);
        final PyObject pyObject3 = py.getModule("sampleQuestionGenerator");
        final Intent question3 = new Intent(this, questionStyle.class);
        TextView deleteLater = (TextView) findViewById(R.id.deleteLater);
        final PyObject pyObject5 = py.getModule("leaderboard");
        submitAnswer.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                String answer = answerEntry.getText().toString();
                PyObject py1 = pyObject3.callAttr("userValidation", question, answer);
                TextView textCheck = (TextView) findViewById(R.id.outputCheck);
                textCheck.setText(py1.toString());
                PyObject py5= pyObject5.callAttr("update", MainActivity.usernameFinal);
                deleteLater.setText(py5.toString());
//                TextView add = (EditText) findViewById(R.id.add1);
//                String a = add.getText().toString();
//                add = (EditText) findViewById(R.id.add2);
//                String b = add.getText().toString();
//                add = (EditText) findViewById(R.id.add3);
//                String c = add.getText().toString();
//                add = (EditText) findViewById(R.id.add4);
//                String d = add.getText().toString();
//                add = (EditText) findViewById(R.id.add5);
//                String e = add.getText().toString();
//                outputTest.setText(a);
            }
        });
        Button nextButton1 = (Button) findViewById(R.id.nextButton);
        nextButton1.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Intent intent = getIntent();
                finish();
                startActivity(intent);
            }
        });
    }

    @Override
    public boolean onSupportNavigateUp() {
        NavController navController = Navigation.findNavController(this, R.id.nav_host_fragment_content_question_style);
        return NavigationUI.navigateUp(navController, appBarConfiguration)
                || super.onSupportNavigateUp();
    }
}
