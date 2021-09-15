import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;
import java.util.stream.Collectors;

public class Cinema {

    private static String[] combinations;
    private static int n;
    private static List<String> usable;
    private static boolean[] used;
    private static StringBuilder stringBuilder = new StringBuilder();
    private static String[] positions;

    public static void main(String[] args) throws IOException {
        var reader = new BufferedReader(new InputStreamReader(System.in));

        usable = Arrays.stream(reader.readLine().split(", ")).collect(Collectors.toList());
        positions = new String[usable.size()];
        n = usable.size();
        String line = reader.readLine();
        while (!line.equals("generate")) {

            String[] tokens = line.split(" - ");

            String name = tokens[0];
            int index = Integer.parseInt(tokens[1]);

            positions[index - 1] = name;

            usable.remove(name);

            line = reader.readLine();
        }

        combinations = new String[usable.size()];
        used = new boolean[usable.size()];

        combine(0);

        System.out.println(stringBuilder.toString().trim());
    }

    private static void combine(int index) {
        if (index >= usable.size()) {
            append();
        } else {
            for (int i = 0; i < usable.size(); i++) {
                if (!used[i]) {
                    used[i] = true;
                    combinations[index] = usable.get(i);
                    combine(index + 1);
                    used[i] = false;
                }
            }
        }
    }

    private static void append() {
        int counter = 0;
        StringBuilder line = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (positions[i] != null) {
                line.append(positions[i]).append(" ");
            } else {
                line.append(combinations[counter++]).append(" ");
            }
        }

        stringBuilder.append(line.toString().trim()).append(System.lineSeparator());
    }
}
