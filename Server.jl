#!/usr/bin/env julia
using PyCall

unshift!(PyVector(pyimport("sys")["path"]), "")
@pyimport CopyPasta

server = listen(3001)
while true
    print("Listening...")
    conn = accept(server)
    @async begin
        try
            while true
                line = readline(conn)
                write(conn, join([CopyPasta.generate_copy_pasta(line), "\n"]))
                println("Written.")
            end
        catch err
            print("connection ended with error $err")
        end
    end
end

## main()
