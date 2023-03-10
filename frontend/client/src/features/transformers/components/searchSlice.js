import { createAsyncThunk, createSlice } from "@reduxjs/toolkit";

import axios from '@/api/axios';


export const search = createAsyncThunk(
    'search/search',
    async (_, thunkAPI) => {

        const { getState } = thunkAPI;
        const state = getState();
        const filters = state.search.filters;
        const sorting = state.search.sorting;
        const pageSize = state.search.pagination.rowsPerPage;
        const pageNumber = state.search.pagination.pageNumber + 1;

        const body = {
            ...filters,
            ...sorting,
        };

        try {
            const res = await axios.post(`/api/transformers/search/?page=${pageNumber}&page_size=${pageSize}`, body);
      
            const data = res.data;

            if (res.status === 200) {
                const page = {
                    'count': +data.count,
                    'results': data.results,
                    'availableFilters': data.available_filters
                };
                const ret = {
                    'page': page,
                    'responseTime': data.response_time
                };
                return ret;
            }
            else {
                return thunkAPI.rejectWithValue(data);
            }
          } 
          catch (err) {
              return thunkAPI.rejectWithValue(err.response.data);
          }
    }
);


export const getAvailableFilters = createAsyncThunk(
    'search/getAvailableFilters',
    async (_, thunkAPI) => {

        try {
            const res = await axios.get(`/api/transformers/get-filters/`);
      
            const data = res.data;

            if (res.status === 200) {
                return data;
            }
            else {
                return thunkAPI.rejectWithValue(data);
            }
          } 
          catch (err) {
              return thunkAPI.rejectWithValue(err.response.data);
          }
    }
);


const initialState = {
    loading: false,
    filters: {
        'search': '',
        'toyline': [],
        'subline': [],
        'size_class': [],
        'manufacturer': [],
        'release_date': [null, null],
        'future_releases': true,
        'price': [null, null],
    },
    availableFilters: null,
    page: null,
    pagination: {
        rowsPerPage: 5,
        pageNumber: 0
    },
    sorting: {
        order: '',
        ascending: 'true'
    },
    responseTime: 0.0,
    errors: null,
};

const searchSlice = createSlice({
    name: 'search',
    initialState,
    reducers: {
        updateOrderBy: (state, action) => {
            state.sorting.order = action.payload;
        },
        updateAscending: (state, action) => {
            state.sorting.ascending = action.payload;
        },
        updatePageNumber: (state, action) => {
            state.pagination.pageNumber = action.payload;
        },
        updateRowsPerPage: (state, action) => {
            state.pagination.rowsPerPage = action.payload;
        },
        updateFilter: (state, action) => {
            state.filters[action.payload.key] = action.payload.value;
        },
        updateSearchFilter: (state, action) => {
            state.filters.search = action.payload;
        },
        updateToylineFilter: (state, action) => {
            state.filters.toyline = action.payload;
        },
        updateSublineFilter: (state, action) => {
            state.filters.subline = action.payload;
        },
        updateSizeClassFilter: (state, action) => {
            state.filters.size_class = action.payload;
        },
        updateManufacturerFilter: (state, action) => {
            state.filters.manufacturer = action.payload;
        },
        updateReleaseDateFilter: (state, action) => {
            state.filters.release_date = action.payload;
        },
        updateFutureReleasesFilter: (state, action) => {
            state.filters.future_releases = action.payload;
        },
        updatePriceFilter: (state, action) => {
            state.filters.price = action.payload;
        },
        resetSearchState: () => initialState,
    },
    extraReducers: builder => {
        builder
            .addCase(search.pending, state => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(search.fulfilled, (state, action) => {
                state.page = action.payload.page;
                state.responseTime = action.payload.responseTime;
                state.loading = false;
                state.errors = null;
            })
            .addCase(search.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
            .addCase(getAvailableFilters.pending, state => {
                state.loading = true;
                state.errors = null;
            })
            .addCase(getAvailableFilters.fulfilled, (state, action) => {
                state.availableFilters = action.payload;
                state.loading = false;
                state.errors = null;
            })
            .addCase(getAvailableFilters.rejected, (state, action) => {
                state.loading = false;
                state.errors = action.payload;
            })
    }
});

export const {
    updateOrderBy,
    updateAscending,
    updatePageNumber,
    updateRowsPerPage,
    updateSearchFilter, 
    updateToylineFilter, 
    updateSublineFilter,
    updateSizeClassFilter, 
    updateManufacturerFilter,
    updateReleaseDateFilter,
    updateFutureReleasesFilter,
    updatePriceFilter,
    updateFilter,
    resetSearchState
} = searchSlice.actions;
export const searchReducer = searchSlice.reducer;