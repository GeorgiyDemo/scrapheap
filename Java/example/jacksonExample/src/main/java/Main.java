import com.fasterxml.jackson.core.JsonProcessingException;
import com.fasterxml.jackson.databind.ObjectMapper;

public class Main {
    private static ObjectMapper mapper;

    public static void reader(String value){
        try {
            String className = mapper.readValue(value,Object.class).getClass().getName();
            System.out.println(className);
        }
        catch (JsonProcessingException e){
            System.out.println("НЕ УДАЛОСЬ ПРЕОБРАЗОВАТЬ "+value);
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        mapper = new ObjectMapper();
        reader("123");
        reader("true");
        reader("\"processing\"");
    }
}
