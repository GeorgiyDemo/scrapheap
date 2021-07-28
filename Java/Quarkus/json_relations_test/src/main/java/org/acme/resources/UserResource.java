package org.acme.resources;

import org.acme.entities.UserEntity;
import org.acme.services.UserService;

import javax.inject.Inject;
import javax.validation.Valid;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.List;
import java.util.Optional;

@Path("/users")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class UserResource {
    
    @Inject
    UserService userService;

    @GET
    public Response getAll() {
        List<UserEntity> allItems = userService.findAll();
        return Response.ok(allItems).build();
    }

    @GET
    @Path("{id}")
    public Response getById(@PathParam("id") Long id) {
        Optional<UserEntity> currentItem = userService.findById(id);
        if (currentItem.isEmpty()) {
            return Response.noContent().build();
        }
        return Response.ok(currentItem.get()).build();
    }

    @PUT
    public Response update(@Valid UserEntity updatedItem) {
        Optional<UserEntity> currentItem = userService.findById(updatedItem.id);
        if (currentItem.isEmpty()) {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
        try {
            userService.update(updatedItem);
            return Response.ok(updatedItem).build();
        } catch (Exception e) {
            return Response.status(Response.Status.BAD_REQUEST).build();
        }
    }

    @POST
    public Response create(@Valid UserEntity newItem) {
        System.out.println(newItem);
        userService.create(newItem);
        return Response.ok(newItem).build();
    }

    @DELETE
    @Path("{id}")
    public Response delete(@PathParam("id") Long id) {
        userService.delete(id);
        return Response.noContent().build();
    }
}