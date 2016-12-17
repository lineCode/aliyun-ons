{
  "targets": [
    {
      "target_name": "ons",
      "sources": [
        "src/entry.cpp",
        "src/log_util.cpp",
        "src/ons_options.cpp",
        "src/consumer_ack.cpp",
        "src/consumer.cpp",
        "src/producer.cpp",
        "src/real_producer_wrapper.cpp",
        "src/consumer_listener.cpp"
      ],
      "include_dirs": [
        "src/third_party/include",
        "<!(node -e \"require('nan')\")"
      ],
      "conditions": [
        ["OS==\"mac\"", {
          "cflags!": [ "-fno-exceptions" ],
          "cflags_cc!": [ "-fno-exceptions", "-pthread", "-Wl,--no-as-needed", "-ldl" ],
          "cflags_cc": [ "-Wno-ignored-qualifiers" ],
          "cflags": [ "-std=c++11", "-stdlib=libc++" ],
          "sources": [ "src/third_party/sole/sole.cpp" ],
          "include_dirs": [
            "/Applications/Xcode.app/Contents/Developer/Toolchains/XcodeDefault.xctoolchain/usr/include/c++/v1",
            "src/third_party/sole"
          ],
          "xcode_settings": {
            "GCC_ENABLE_CPP_EXCEPTIONS": "YES"
          }
        }],
        ["OS==\"linux\"", {
          "sources": [ "src/third_party/sole/sole.cpp" ],
          "include_dirs": [ "src/third_party/sole" ],
          "libraries": [
            "../src/third_party/lib/linux/libonsclient4cpp.a"
          ],
          "cflags_cc!": [ "-fno-exceptions", "-pthread", "-Wl,--no-as-needed", "-ldl" ],
          "cflags_cc": [ "-Wno-ignored-qualifiers" ],
          "cflags": [ "-std=c++11", "-g" ]
        }],
        ["OS==\"win\"", {
          "libraries": [
            "../src/third_party/lib/windows/ONSClient4CPP.lib"
          ],
          "copies": [
            {
              "destination": "<(module_root_dir)/build/Release/",
              "files": [ "<(module_root_dir)/src/third_party/lib/windows/ONSClient4CPP.dll" ]
            }
          ]
        }]
      ]
    }
  ]
}
