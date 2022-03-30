package com.demka.retrofitexample;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.widget.TextView;

import java.util.List;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;
import retrofit2.Retrofit;
import retrofit2.converter.gson.GsonConverterFactory;

public class MainActivity extends AppCompatActivity {

    TextView textView;
    String baseUrl = "https://jsonplaceholder.typicode.com/";
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        textView = findViewById(R.id.textjsondata);
        textView.setText("");

        //Create Retrofit object
        Retrofit retrofit = new Retrofit.Builder().baseUrl(baseUrl).addConverterFactory(GsonConverterFactory.create()).build();

        //Convert json data to model
        MyApi myApi = retrofit.create(MyApi.class);

        //Create a call of model
        Call<List<Model>> call = myApi.getModels();

        call.enqueue(new Callback<List<Model>>() {
            @Override
            public void onResponse(Call<List<Model>> call, Response<List<Model>> response) {

                List<Model> data = response.body();

                for (Model item: data) {
                    textView.append(item.title+"\n"+item.body+"\n\n");
                }

            }

            @Override
            public void onFailure(Call<List<Model>> call, Throwable t) {

            }
        });

    }
}