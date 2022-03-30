package com.demka.retrofitexample;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.GET;

public interface MyApi {

    @GET("posts")
    Call<List<Model>> getModels();
}
