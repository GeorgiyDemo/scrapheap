package org.acme;

import javax.inject.Inject;
import javax.validation.Valid;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;
import java.util.List;
import java.util.Optional;


@Path("/tasks")
@Produces(MediaType.APPLICATION_JSON)
@Consumes(MediaType.APPLICATION_JSON)
public class TaskResource {


    @Inject
    TaskService taskService;

    @GET
    public Response getAll() {
        List<TaskEntity> allItems = taskService.findAll();
        return Response.ok(allItems).build();
    }

    @GET
    @Path("{id}")
    public Response getById(@PathParam("id") Long id) {
        Optional<TaskEntity> currentItem = taskService.findById(id);
        if (currentItem.isEmpty()) {
            return Response.noContent().build();
        }
        return Response.ok(currentItem.get()).build();
    }

    @PUT
    public Response update(@Valid TaskEntity updatedItem) {
        Optional<TaskEntity> currentItem = taskService.findById(updatedItem.id);
        if (currentItem.isEmpty()) {
            return Response.status(Response.Status.NOT_FOUND).build();
        }
        try {
            taskService.update(updatedItem);
            return Response.ok(updatedItem).build();
        } catch (Exception e) {
            return Response.status(Response.Status.BAD_REQUEST).build();
        }
    }

    @POST
    public Response create(@Valid TaskEntity newItem) {
        System.out.println(newItem);
        taskService.create(newItem);
        return Response.ok(newItem).build();
    }

    @DELETE
    @Path("{id}")
    public Response delete(@PathParam("id") Long id) {
        taskService.delete(id);
        return Response.noContent().build();
    }
}
